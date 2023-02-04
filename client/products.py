from nicegui import ui, Client
from client.dialog import new_product
from client.global_layout import globalLayout
from javascript.fetch_api import fetch_api
from javascript.table import defaultColDef
from style.page_title import ui_page_title

products_table: ui.table


async def load_data_from_api():
    data = await fetch_api("products")
    products_table.options["rowData"] = data
    products_table.update()


@ui.page(path="/client/products", title="Produtos")
async def products(client: Client):
    global products_table
    globalLayout()
    with ui.card().style(add="width: 100%; height: 95vh;"):
        ui_page_title("Produtos")

        products_table = ui.table(
            {
                "defaultColDef": defaultColDef(),
                "columnDefs": [
                    {"headerName": "Nome", "field": "name"},
                    {"headerName": "Marca", "field": "brand"},
                ],
                "defaultColGroupDef": {
                    "marryChildren": True,
                },
                "rowSelection": "single",
                "rowData": [],
            }
        )
        client.on_connect(load_data_from_api)  # load data and update table

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button("Cadastrar Produto", on_click=lambda: new_product.dialog().open())
            with ui.row():
                ui.button("Editar").style(add="width: 8rem;")
                ui.button("Remover").style(add="width: 8rem;")
