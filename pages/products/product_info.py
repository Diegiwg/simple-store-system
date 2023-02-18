from nicegui import ui

import api
import components
import functions
import models
import styles

form_data: models.Product
dialog_instance: ui.dialog
products_table_instance: ui.table


async def load_form_data():
    global form_data
    data = await products_table_instance.get_selected_row()
    if data is None:
        return False

    form_data = models.Product(
        id=data["id"],
        name=data["name"],
        brand=data["brand"],
        reference=data["reference"],
        price=data["price"],
    )

    return True


def form_input(label: str, bind_value: str):
    return (
        ui.input(label)
        .bind_value(target_object=form_data, target_name=bind_value)
        .props(add="autofocus filled dense='dense' ")
    )


async def form_validation():
    if (
        form_data.name is None
        or form_data.brand is None
        or form_data.reference is None
        or form_data.price is None
        or form_data.price == 0.00
    ):
        return False
    return True


async def edit_product_handler():
    global form_data, dialog_instance

    if await form_validation() is False:
        ui.notify(message="Informações do Produto estão incompletas!", type="negative")
        return

    api.products.edit(form_data)

    ui.notify("Produto atualizado com sucesso!", type="positive")

    dialog_instance.close()
    functions.table.update_data_from_api(api.products, products_table_instance)
    form_data = models.Product(price=0.00)


async def new_product_handler():
    global form_data, dialog_instance
    if await form_validation() is False:
        ui.notify(message="Informações do Produto estão incompletas!", type="negative")
        return

    api.products.create(
        form_data.name, form_data.brand, form_data.reference, form_data.price
    )

    ui.notify("Produto cadastrado com sucesso!", type="positive")

    dialog_instance.close()
    functions.table.update_data_from_api(api.products, products_table_instance)
    form_data = models.Product(price=0.00)


DIALOG = {
    "new": {
        "page_title": "Novo Produto",
        "action": "Cadastrar",
        "handler": new_product_handler,
    },
    "edit": {
        "page_title": "Editar Produto",
        "action": "Editar",
        "handler": edit_product_handler,
    },
}


class product_dialog:
    def __init__(self, products_table: ui.table, product_info=None) -> None:
        self.products_table = products_table
        self.product_info = product_info

    async def run(self):
        global dialog_instance, products_table_instance, form_data
        products_table_instance = self.products_table

        dialog_type = "edit"
        if self.product_info is None:
            form_data = models.Product(price=0.00)
            dialog_type = "new"
        else:
            if await load_form_data() is False:
                return

        with ui.dialog() as dialog, ui.card() as card:
            dialog_instance = dialog

            components.page_title(DIALOG[dialog_type]["page_title"])

            form_input("Nome do Produto", "name")
            form_input("Marca do Produto", "brand")
            form_input("Referencia do Produto", "reference")
            form_input("Preço do Produto", "price")

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

            styles.Sizing(card).width("w-max")
            styles.Layout(card).display("flex")
            styles.FlexboxGrid(card).flex_direction("flex-col").align_items(
                "items-stretch"
            )

        dialog.open()
