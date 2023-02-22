from nicegui import ui

import api
import functions
import styles

from .state import state


def products_table_data():
    print("Updating products table data...")
    data = []
    for product in api.products.get_all():
        if not product.stock or product.id in state.current_cart_ids:
            continue

        data.append(product.to_dict())

    return data


async def handle_add_to_cart():
    product = await state.add_product_to_cart_table.get_selected_row()

    if state.add_product_to_cart_quantity_value > product["stock"]["quantity"]:
        ui.notify(message="Quantidade em estoque insuficiente!", type="negative")
        return

    product["quantity"] = state.add_product_to_cart_quantity_value

    state.current_cart.append(product)
    state.current_cart_ids.append(product["id"])

    functions.table.refresh_table(state.current_cart_table, state.current_cart)

    state.add_product_to_cart_quantity_value = 1
    state.add_product_to_cart_dialog.close()


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
    "rowData": [],
}


def generator_table() -> ui.table:
    state.add_product_to_cart_table = ui.table(PRODUCT_TABLE_CONFIG)
    functions.table.refresh_table(
        state.add_product_to_cart_table, products_table_data()
    )
    return state.add_product_to_cart_table


def add_product_to_cart_table():
    with ui.dialog() as dialog, styles.Sizing(ui.card()).width("w-full").element:
        ui.label("Adicionar Produto ao Carrinho")

        generator_table()

        with ui.row() as el:
            styles.Sizing(el).width("w-full")
            styles.FlexboxGrid(el).align_items("items-center").justify_content(
                "justify-between"
            )

            ui.number(label="Quantidade", value=1).bind_value(
                target_object=state, target_name="add_product_to_cart_quantity_value"
            )
            ui.button("Adicionar Produto", on_click=handle_add_to_cart)

    state.add_product_to_cart_dialog = dialog
    dialog.open()
