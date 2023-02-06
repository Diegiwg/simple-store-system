from nicegui import ui

import api
import components


class FormData:
    def __init__(self):
        self.name = ""
        self.brand = ""
        self.reference = ""
        self.price = 0.0


form_data = FormData()
dialog_instance: ui.dialog
products_table_instance: ui.table


def load_data_from_api():
    data = api.products.get_all()
    products_table_instance.options["rowData"] = data
    products_table_instance.update()


async def new_product_handler():
    global form_data, dialog_instance

    if (
        form_data.name == ""
        or form_data.brand == ""
        or form_data.reference == ""
        or form_data.price == 0.0
    ):
        ui.notify(message="Informações do Produto estão incompletas!", type="negative")
        return

    api.products.new(
        form_data.name, form_data.brand, form_data.reference, form_data.price
    )
    load_data_from_api()

    form_data = FormData()

    ui.notify("Produto cadastrado com sucesso!", type="positive")
    dialog_instance.close()


def new_product(products_table: ui.table):
    global dialog_instance, products_table_instance
    with ui.dialog() as dl, ui.card().style(
        add="width: 100%; display: flex; flex-direction: column; align-items: stretch;"
    ):

        dialog_instance = dl
        products_table_instance = products_table
        components.page_title("Novo Produto")

        ui.input(label="Nome do Produto").bind_value(
            target_object=form_data, target_name="name"
        ).props(add="autofocus filled dense='dense' ")

        ui.input(label="Marca do Produto").bind_value(
            target_object=form_data, target_name="brand"
        ).props(add="filled dense='dense' ")

        ui.input(label="Referencia do Produto").bind_value(
            target_object=form_data, target_name="reference"
        ).props(add="filled dense='dense' ")

        ui.number(label="Preço do Produto", format="%.2f").bind_value(
            target_object=form_data, target_name="price"
        ).props(add="filled dense='dense' ")

        with ui.row().style(add="display: flex; justify-content: flex-end;"):
            ui.button(text="Cancelar", on_click=dl.close).style(
                add="width: 8rem; background-color: #ac0d0d !important;"
            )
            ui.button(text="Cadastrar", on_click=new_product_handler).style(
                add="width: 8rem;"
            )

        return dl
