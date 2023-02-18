from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
import styles
from routes import Route, route_manager

from .product_info import product_dialog

table_instance: ui.table


async def delete_product_item():
    item = await table_instance.get_selected_row()
    if item is None:
        return
    api.products.delete(item["id"])
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
                on_click=product_dialog(table_instance).run,
            )
            with ui.row():
                edit_btn = ui.button(
                    "Editar",
                    on_click=product_dialog(
                        products_table=table_instance,
                        product_info=True,
                    ).run,
                )
                remove_btn = ui.button("Remover", on_click=delete_product_item)

                btn_sizing = styles.Sizing().width("w-32")
                btn_sizing.apply(edit_btn)
                btn_sizing.apply(remove_btn)


products_route = Route("products", "Produtos", page)
route_manager.register_route(products_route)
