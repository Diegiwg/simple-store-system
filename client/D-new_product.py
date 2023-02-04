from nicegui import ui
from client.global_layout import globalLayout
from style.page_title import ui_page_title


class FormData:
    def __init__(self):
        self.name = ""
        self.brand = ""
        self.reference = ""
        self.price = 0.0


form_data = FormData()


async def new_product_handler():
    if (
        form_data.name == ""
        or form_data.brand == ""
        or form_data.reference == ""
        or form_data.price == 0.0
    ):
        ui.notify(message="Informações do Produto estão incompletas!", type="negative")
        return

    ui.notify(message=f"Product {form_data.name} added")


@ui.page(path="/client/new_product", title="Novo Produto")
async def new_product():
    globalLayout()
    with ui.card().style(
        add="width: 60%; display: flex; flex-direction: column; align-items: stretch;"
    ):

        ui_page_title("Novo Produto")

        ui.separator()

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
            ui.button(text="Cancelar", on_click=lambda: ui.open("/")).style(
                add="width: 8rem; background-color: #ac0d0d !important;"
            )
            ui.button(text="Cadastrar", on_click=new_product_handler).style(
                add="width: 8rem;"
            )

        ui.separator()
