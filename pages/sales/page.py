from nicegui import ui

import components
import functions
import styles
from routes import Route, route_manager

from .dialog_add_product_to_cart import add_product_to_cart_table
from .dialog_edit_product_in_cart import edit_product_in_cart
from .state import state


async def handle_remove_from_cart():
    product = await state.current_cart_table.get_selected_row()

    if product is None:
        return

    state.current_cart.remove(product)
    state.current_cart_ids.remove(product["id"])

    functions.table.refresh_table(state.current_cart_table, state.current_cart)


async def handle_clear_cart():
    state.current_cart = []
    state.current_cart_ids = []
    functions.table.refresh_table(state.current_cart_table, state.current_cart)


PRODUCT_TABLE_CONFIG = {
    "defaultColDef": functions.table.default_col_def(),
    "columnDefs": [
        {"headerName": "Quantidade", "field": "quantity"},
        {"headerName": "Nome", "field": "name"},
        {"headerName": "Marca", "field": "brand"},
        {"headerName": "Referencia", "field": "reference"},
        {"headerName": "Preço", "field": "price"},
    ],
    "rowSelection": "single",
    "rowData": state.current_cart,
}


def generator_table() -> ui.table:
    table = ui.table(PRODUCT_TABLE_CONFIG)
    return styles.Sizing(table).width("w-full").height("h-96").element


def generator_buttons(name: str, callback):
    btn = ui.button(name, on_click=callback)
    return styles.Sizing(btn).width("w-52").element


async def page():
    with route_manager.root_element:
        components.page_title(route_manager.current_route.title)

        ui.label("Produtos no Carrinho")

        state.current_cart_table = generator_table()

        with ui.row() as el:
            styles.Sizing(el).width("w-full")
            styles.FlexboxGrid(el).justify_content("justify-between")

            with ui.column():
                generator_buttons("Adicionar Produto", add_product_to_cart_table)
                generator_buttons("Editar Produto", edit_product_in_cart)
                generator_buttons("Remover Produto", handle_remove_from_cart)

            with ui.column():
                generator_buttons("Limpar Carrinho", handle_clear_cart)
                generator_buttons("Concluir Venda", None)


sales_route = Route("sales", "Vendas", page)
route_manager.register_route(sales_route)
