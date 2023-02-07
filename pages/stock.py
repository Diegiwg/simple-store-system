from nicegui import ui
from nicegui.page import globals

import api
import components
import routes
from javascript import table

stock_table: ui.table


def load_data_from_api():
    data = api.stock.get_all()
    stock_table.options["rowData"] = data
    stock_table.update()


async def delete_stock_item():
    item = await table.get_selected_rows(stock_table.id)
    print(item)
    if item is None:
        return
    api.stock.delete(item)
    load_data_from_api()


async def page():
    global stock_table

    with ui.column().style(add="width: 100%; height: 95vh;") as element:
        globals.title = routes.route_manager.current_route.title
        components.page_title(routes.route_manager.current_route.title)

        stock_table = ui.table(
            options={
                "defaultColDef": table.default_col_def(),
                "columnDefs": [
                    {
                        "headerName": "ID",
                        "field": "id",
                        "filter": False,
                    },
                    {"headerName": "Nome do Produto", "field": "name"},
                    {"headerName": "Quantidade", "field": "quantity"},
                ],
                "rowSelection": "single",
                "rowData": [],
            },
        ).style(add="height: 74vh;")
        load_data_from_api()  # load data and update table

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button(
                "Adicionar Produto",
                on_click=components.modal_new_stock(stock_table).open,
            )
            with ui.row():
                ui.button(text="Editar").style(add="width: 8rem;")
                ui.button(text="Remover", on_click=delete_stock_item).style(
                    add="width: 8rem;"
                )
    return element


stock_route = routes.Route("stock", "Estoque", page)
routes.route_manager.register_route(stock_route)
