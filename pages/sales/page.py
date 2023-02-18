from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
from routes import Route, route_manager

from .components import new_product_to_cart


class State:
    def __init__(self) -> None:
        self.current_cart = []
        self.table = ui.table({})


state = State()


def product_table_data():
    data = []
    for product in api.products.get_all():
        if not product.stock or product.id not in state.current_cart:
            continue

        data.append(product.to_dict())
    return data


async def add_to_cart():
    await new_product_to_cart.render(state)


async def remove_from_cart():
    product = await state.table.get_selected_row()
    state.current_cart.remove(product["id"])

    functions.table.refresh_table(state.table, product_table_data())


async def clear_cart():
    print(state.current_cart)
    state.current_cart.clear()
    functions.table.refresh_table(state.table, product_table_data())


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


async def page():
    with route_manager.root_element:
        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

        ui.label("Produtos no Carrinho")
        state.table = ui.table(PRODUCT_TABLE_CONFIG)

        with ui.row():
            ui.button("Adicionar Produto", on_click=add_to_cart)
            ui.button("Limpar Carrinho", on_click=clear_cart)
            ui.button("Concluir Venda")


sales_route = Route("sales", "Vendas", page)
route_manager.register_route(sales_route)
