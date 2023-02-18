from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
import styles
from routes import Route, route_manager

from .stock_info import stock_dialog

stock_table: ui.table


async def delete_stock_item():
    item = await stock_table.get_selected_row()
    if item is None:
        return
    api.stock.delete(item["stock"]["id"])
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
                on_click=stock_dialog(stock_table).run,
            )
            with ui.row():
                edit_btn = ui.button(
                    text="Editar",
                    on_click=stock_dialog(stock_table, stock_table.id).run,
                )
                remove_btn = ui.button(text="Remover", on_click=delete_stock_item)

                btn_sizing = styles.Sizing().width("w-32")
                btn_sizing.apply(edit_btn)
                btn_sizing.apply(remove_btn)


stock_route = Route("stock", "Estoque", page)
route_manager.register_route(stock_route)
