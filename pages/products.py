from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
import javascript
from routes import Route, route_manager

table_instance: ui.table


async def delete_product_item():
    item = await javascript.table.get_selected_rows(table_instance.id)
    if item is None:
        return
    api.products.delete(item)
    functions.table.update_data_from_api(api.products, table_instance)


async def page():
    global table_instance

    with route_manager.root_element:

        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

        table_instance = ui.table(
            {
                "defaultColDef": functions.table.default_col_def(),
                "columnDefs": [
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
        functions.table.update_data_from_api(api.products, table_instance)

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
