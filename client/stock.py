from nicegui import Client, ui

import components
from client import layout
from javascript import fetch_api, table

stock_table: ui.table


async def load_data_from_api():
    data = await fetch_api("stock")
    stock_table.options["rowData"] = data
    stock_table.update()


async def check_marked_item():
    selected_row: list = await table.get_selected_row(stock_table.id)
    if len(selected_row) == 0:
        ui.notify("Nehum Produto selecionado!", type="negative")

    return selected_row


@ui.page(path="/client/stock", title="Estoque")
async def stock(client: Client):
    global stock_table
    client.on_connect(layout.render)

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Estoque")

        stock_table = ui.table(
            options={
                "defaultColDef": table.default_col_def(),
                "columnDefs": [
                    {
                        "headerName": "ID",
                        "field": "id",
                        "filter": False,
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
