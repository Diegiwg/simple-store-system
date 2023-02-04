from nicegui import ui, Client
from client.global_layout import globalLayout
from javascript.fetch_api import fetch_api
from javascript.table import defaultColDef, get_selected_row

from style.page_title import ui_page_title

stock_table: ui.table


async def load_data_from_api():
    data = await fetch_api("stock")
    stock_table.options["rowData"] = data
    stock_table.update()


async def check_marked_item():
    selected_row: list = await get_selected_row(stock_table.id)
    if len(selected_row) == 0:
        ui.notify("Nehum Produto selecionado!", type="negative")

    return selected_row


@ui.page(path="/client/stock", title="Estoque")
async def stock(client: Client):
    global stock_table
    globalLayout()

    with ui.card().style(add="width: 100%; height: 95vh;"):
        ui_page_title("Estoque")

        stock_table = ui.table(
            options={
                "defaultColDef": defaultColDef(),
                "columnDefs": [
                    {
                        "headerName": "ID",
                        "field": "id",
                        "filter": False,
                        "floatingFilter": False,
                        "width": 10,
                    },
                    {"headerName": "Nome do Produto", "field": "name"},
                    {"headerName": "Quantidade", "field": "quantity"},
                ],
                "rowSelection": "single",
                "rowData": [],
            },
        )
        client.on_connect(load_data_from_api)  # load data and update table

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button("Adicionar Produto")
            with ui.row():
                ui.button("Editar", on_click=check_marked_item).style(
                    add="width: 8rem;"
                )
                ui.button("Remover", on_click=check_marked_item).style(
                    add="width: 8rem;"
                )
