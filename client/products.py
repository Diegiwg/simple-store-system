from nicegui import Client, ui

import api
import components
from client import dialog, layout
from javascript import table

products_table: ui.table


def load_data_from_api():
    data = api.products.get_products()
    products_table.options["rowData"] = data
    products_table.update()


@ui.page(path="/client/products", title="Produtos")
async def products(client: Client):
    global products_table
    client.on_connect(layout.render)

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Produtos")

        products_table = ui.table(
            {
                "defaultColDef": table.default_col_def(),
                "columnDefs": [
                    {"headerName": "ID", "field": "id", "filter": False, "width": 30},
                    {"headerName": "Nome", "field": "name"},
                    {"headerName": "Marca", "field": "brand", "width": 100},
                    {"headerName": "Referencia", "field": "reference", "width": 100},
                    {"headerName": "Preço", "field": "price", "width": 100},
                ],
                "defaultColGroupDef": {
                    "marryChildren": True,
                },
                "rowSelection": "single",
                "rowData": [],
            }
        ).style(add="height: 74vh;")
        client.on_connect(load_data_from_api)  # load data and update table

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button(
                "Cadastrar Produto",
                on_click=lambda: dialog.new_product(products_table).open(),
            )
            with ui.row():
                ui.button("Editar").style(add="width: 8rem;")
                ui.button("Remover").style(add="width: 8rem;")
