from nicegui import Client, ui

import api
import components
from javascript import table

table_instance: ui.table


def load_data_from_api():
    data = api.products.get_all()
    table_instance.options["rowData"] = data
    table_instance.update()


async def delete_product_item():
    item = await table.get_selected_rows(table_instance.id)
    print(item)
    if item is None:
        return
    api.products.delete(item)
    load_data_from_api()


@ui.page(path="/products", title="Produtos")
async def render(client: Client):
    global table_instance
    client.on_connect(components.render_layout)

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Produtos")

        table_instance = ui.table(
            {
                "defaultColDef": table.default_col_def(),
                "columnDefs": [
                    {
                        "headerName": "ID",
                        "field": "id",
                        "filter": False,
                    },
                    {"headerName": "Nome", "field": "name"},
                    {"headerName": "Marca", "field": "brand"},
                    {"headerName": "Referencia", "field": "reference"},
                    {
                        "headerName": "Preço",
                        "field": "price",
                    },
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
                on_click=lambda: components.modal_new_product(table_instance).open(),
            )
            with ui.row():
                ui.button("Editar").style(add="width: 8rem;")
                ui.button("Remover", on_click=delete_product_item).style(
                    add="width: 8rem;"
                )
