from nicegui import ui
from nicegui.page import globals

import api
import components
import functions
import models
from routes import Route, route_manager
from styles import *


class sales_space:
    def __init__(self):
        self.current_cart = []
        self.table: ui.table


sales = sales_space()


def product_table_data():
    data: models.Product = []
    for product in api.products.get_all():
        if not product.stock or product.id in sales.current_cart:
            print(product.name)
            continue

        data.append(product.to_dict())
    return data


async def add_to_cart():
    global sales
    product = await sales.table.get_selected_row()
    sales.current_cart.append(product["id"])

    functions.table.refresh_table(sales.table, product_table_data())


async def remove_from_cart():
    global sales
    product = await sales.table.get_selected_row()
    sales.current_cart.remove(product["id"])

    functions.table.refresh_table(sales.table, product_table_data())


async def clear_cart():
    global sales
    sales.current_cart = []

    functions.table.refresh_table(sales.table, product_table_data())


async def page():
    global sales
    sales = sales_space()

    with route_manager.root_element:
        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

        data = product_table_data()

        sales.table = ui.table(
            {
                "defaultColDef": functions.table.default_col_def(),
                "columnDefs": [
                    {"headerName": "Estoque", "field": "stock.quantity"},
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
                "rowData": data,
            }
        ).style(add="height: 30vh;")

        with ui.row():
            ui.number()
            ui.button("Adicionar Produto", on_click=add_to_cart)

        with ui.row():
            ui.button("Limpar Carrinho", on_click=clear_cart)
            ui.button("Concluir Venda")


sales_route = Route("sales", "Vendas", page)
route_manager.register_route(sales_route)
