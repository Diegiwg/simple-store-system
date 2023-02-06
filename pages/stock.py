from nicegui import Client, ui

import api
import components
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


@ui.page(path="/stock", title="Estoque")
async def render(client: Client):
    global stock_table
    client.on_connect(components.render_layout)

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
                    },
                    {"headerName": "Nome do Produto", "field": "name"},
                    {"headerName": "Quantidade", "field": "quantity"},
                ],
                "rowSelection": "single",
                "rowData": [],
            },
        ).style(add="height: 74vh;")
        client.on_connect(load_data_from_api)  # load data and update table

        with ui.row().style(
            add="width: 100%; display: flex; justify-content: space-between;"
        ):
            ui.button(
                "Adicionar Produto",
                on_click=components.modal_new_stock(
                    table_instance=stock_table, client_instance=client
                ).open,
            )
            with ui.row():
                ui.button(text="Editar").style(add="width: 8rem;")
                ui.button(text="Remover", on_click=delete_stock_item).style(
                    add="width: 8rem;"
                )
