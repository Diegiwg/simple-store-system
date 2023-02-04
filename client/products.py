from nicegui import Client, ui

import components
from client import dialog, layout
from javascript import fetch_api, table

products_table: ui.table


async def load_data_from_api():
    data = await fetch_api("products")
    products_table.options["rowData"] = data
    products_table.update()


@ui.page(path="/client/products", title="Produtos")
async def products(client: Client):
    global products_table
    layout.render()

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Produtos")

        products_table = ui.table(
            {
                "defaultColDef": table.default_col_def(),
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
            ui.button("Cadastrar Produto", on_click=lambda: dialog.new_product().open())
            with ui.row():
                ui.button("Editar").style(add="width: 8rem;")
                ui.button("Remover").style(add="width: 8rem;")
