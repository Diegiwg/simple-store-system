from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
from routes import Route, route_manager
import javascript

stock_table: ui.table


async def delete_stock_item():
    item = await javascript.table.get_selected_rows(stock_table.id)
    if item is None:
        return
    api.stock.delete(item)
    functions.table.update_data_from_api(api.stock, stock_table)


async def page():
    global stock_table

    with route_manager.root_element:
        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

        stock_table = ui.table(
            options={
                "defaultColDef": functions.table.default_col_def(),
                "columnDefs": [
                    {"headerName": "Nome do Produto", "field": "name"},
                    {"headerName": "Quantidade", "field": "stock.quantity"},
                ],
                "rowSelection": "single",
                "rowData": [],
            },
        ).style(add="height: 74vh;")
        functions.table.update_data_from_api(api.stock, stock_table)

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button(
                "Adicionar Produto",
                on_click=lambda: components.modal_new_stock(stock_table).open(),
            )
            with ui.row():
                ui.button(text="Editar").style(add="width: 8rem;")
                ui.button(text="Remover", on_click=delete_stock_item).style(
                    add="width: 8rem;"
                )


stock_route = Route("stock", "Estoque", page)
route_manager.register_route(stock_route)
