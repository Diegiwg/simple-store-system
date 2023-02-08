from nicegui import ui
from nicegui.page import globals

import api
import components
from routes import Route, route_manager
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


async def page():
    global table_instance

    with route_manager.root_element:

        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

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
        load_data_from_api()  # load data and update table

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


products_route = Route("products", "Produtos", page)
route_manager.register_route(products_route)
