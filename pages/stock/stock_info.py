from nicegui import ui

import api
import components
import functions
import styles


class Info:
    def __init__(self, id=None, product=None, quantity=0) -> None:
        self.id = id
        self.product = product
        self.quantity = quantity


form_data: Info
dialog_instance: ui.dialog
product_table: ui.table
stock_table: ui.table


async def load_form_data():
    global form_data, product_table
    data = await stock_table.get_selected_row()
    if data is None:
        return False

    form_data = Info(
        id=data["stock"]["id"],
        product=data,
        quantity=data["stock"]["quantity"],
    )

    return True


async def load_product_table():
    global product_table
    product_table = ui.table(
        options={
            "defaultColDef": functions.table.default_col_def(),
            "columnDefs": [
                {"headerName": "Nome do Produto", "field": "name"},
                {"headerName": "Marca do Produto", "field": "brand"},
                {"headerName": "Referencia do Produto", "field": "reference"},
            ],
            "rowSelection": "single",
            "rowData": api.stock.get_all_without_stock(),
        }
    )
    return product_table


async def form_validation():
    if (
        form_data.quantity is None
        or form_data.quantity == 0
        or form_data.quantity == ""
    ):
        return False
    return True


async def edit_stock_handler():
    global form_data, dialog_instance, product_table, stock_table
    if await form_validation() is False:
        ui.notify(message="A quantidade em estoque não pode ser zero!", type="warning")
        return

    api.stock.edit(form_data)
    ui.notify("Produto adicionado ao Estoque com sucesso!", type="positive")

    dialog_instance.close()
    functions.table.update_data_from_api(api.stock, stock_table)
    form_data = Info()


async def new_stock_handler():
    global form_data, dialog_instance, product_table, stock_table
    if await form_validation() is False:
        ui.notify(message="A quantidade em estoque não pode ser zero!", type="warning")
        return

    form_data.product = await product_table.get_selected_row()
    api.stock.create(form_data.product["id"], form_data.quantity)
    ui.notify("Produto adicionado ao Estoque com sucesso!", type="positive")

    dialog_instance.close()
    functions.table.update_data_from_api(api.stock, stock_table)
    form_data = Info()


DIALOG = {
    "new": {
        "page_title": "Novo Produto em Estoque",
        "action": "Cadastrar",
        "handler": new_stock_handler,
    },
    "edit": {
        "page_title": "Editar Produto em Estoque",
        "action": "Editar",
        "handler": edit_stock_handler,
    },
}


class stock_dialog:
    def __init__(self, table_instance: ui.table, product=None) -> None:
        global stock_table
        stock_table = table_instance
        self.product = product

    async def run(self):
        global form_data, dialog_instance

        dialog_type = "edit"
        if self.product is None:
            form_data = Info()
            dialog_type = "new"
        else:
            if await load_form_data() is False:
                return

        with ui.dialog() as dialog, ui.card() as card:
            dialog_instance = dialog

            components.page_title(DIALOG[dialog_type]["page_title"])

            if dialog_type == "new":
                await load_product_table()
            else:
                ui.input(label=f"Produto:  {form_data.product['name']}").props(
                    add="readonly"
                )

            ui.number(label="Quantidade em Estoque").bind_value(
                form_data, target_name="quantity"
            )

            with ui.row().style(add="display: flex; justify-content: flex-end;"):
                close_btn = ui.button(text="Cancelar", on_click=dialog.close)
                action_btn = ui.button(
                    text=DIALOG[dialog_type]["action"],
                    on_click=DIALOG[dialog_type]["handler"],
                )

                btn_sizing = styles.Sizing().width("w-32")
                btn_sizing.apply(close_btn)
                btn_sizing.apply(action_btn)

                close_btn.style(add="background-color: rgb(153 27 27) !important;")

            styles.Sizing(card).width("w-screen")
            styles.Layout(card).display("flex")
            styles.FlexboxGrid(card).flex_direction("flex-col").align_items(
                "items-stretch"
            )

        dialog.open()
