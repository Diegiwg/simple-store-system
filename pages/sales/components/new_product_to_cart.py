import typing

from nicegui import ui

import api
import functions
import styles


class Context:
    def __init__(self, current_cart: list) -> None:
        self.table: ui.table
        self.current_cart = current_cart


class State:
    def __init__(self):
        self.context = Context([])
        self.product_table: ui.table
        self.product: dict
        self.dialog: ui.dialog


state = State()


def product_table_data():
    data = []
    for product in api.products.get_all():
        if not product.stock or product.id in state.context.current_cart:
            continue

        data.append(product.to_dict())
    return data


PRODUCT_TABLE_CONFIG = {
    "defaultColDef": functions.table.default_col_def(),
    "columnDefs": [
        {"headerName": "Estoque", "field": "stock.quantity"},
        {"headerName": "Nome", "field": "name"},
        {"headerName": "Marca", "field": "brand"},
        {"headerName": "Referencia", "field": "reference"},
        {"headerName": "Preço", "field": "price"},
    ],
    "rowSelection": "single",
    "rowData": product_table_data(),
}


async def select_product():
    product = await state.product_table.get_selected_row()
    if product is None:
        return

    state.context.current_cart.append(product["id"])

    functions.table.refresh_table(
        state.product_table, product_table_data()
    )  # update products table
    functions.table.refresh_table(
        state.context.table, product_table_data()
    )  # update current cart table

    state.dialog.close()


async def render(context):
    with ui.dialog() as dialog, ui.card() as main:

        state.product_table = ui.table(PRODUCT_TABLE_CONFIG)
        ui.number(label="Quantidade")

        ui.button("Adicionar Produto", on_click=select_product)

    styles.Sizing(main).width("w-full")

    state.context = context
    state.dialog = dialog

    state.dialog.open()
