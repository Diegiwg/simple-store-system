from nicegui import ui

import api
import components
import functions
import javascript


class ProductQuantity:
    def __init__(self, quantity) -> None:
        self.quantity = quantity


form_product_quantity = ProductQuantity(0)
internal_table_instance: ui.table
stock_table_instance: ui.table
dialog_instance: ui.dialog


async def new_stock_handler():
    global dialog_instance, form_product_quantity

    if form_product_quantity.quantity == 0:
        ui.notify(message="A quantidade em estoque não pode ser zero!", type="warning")
        return

    product_id = await javascript.table.get_selected_rows(internal_table_instance.id)
    if product_id is None:
        ui.notify(message="Produto não encontrado!", type="negative")
        return

    api.stock.create(product_id, form_product_quantity.quantity)
    form_product_quantity.quantity = 0
    dialog_instance.close()

    functions.table.update_data_from_api(api.stock, stock_table_instance)


def new_stock(table_instance: ui.table):
    global internal_table_instance, stock_table_instance, dialog_instance, form_product_quantity

    with ui.dialog() as dl, ui.card().style(
        add="width: 100%; display: flex; flex-direction: column; align-items: stretch;"
    ):
        dialog_instance = dl
        stock_table_instance = table_instance

        components.page_title("Novo Produto em Estoque")

        internal_table_instance = ui.table(
            options={
                "defaultColDef": functions.table.default_col_def(),
                "columnDefs": [
                    {"headerName": "Nome do Produto", "field": "name"},
                    {"headerName": "Marca do Produto", "field": "brand"},
                    {"headerName": "Refrencia do Produto", "field": "reference"},
                ],
                "rowSelection": "single",
                "rowData": api.stock.get_all_without_stock(),
            }
        )

        ui.number(label="Quantidade em Estoque").bind_value(
            form_product_quantity, target_name="quantity"
        )

        with ui.row().style(add="display: flex; justify-content: flex-end;"):
            ui.button(text="Cancelar", on_click=dl.close).style(
                add="width: 8rem; background-color: #ac0d0d !important;"
            )
            ui.button(text="Cadastrar", on_click=new_stock_handler).style(
                add="width: 8rem;"
            )
    return dl
