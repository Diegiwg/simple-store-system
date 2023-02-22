from nicegui import ui


class State:
    current_cart: list = []
    current_cart_ids: list = []
    current_cart_table: ui.table | None = None

    add_product_to_cart_table: ui.table | None = None
    add_product_to_cart_dialog: ui.dialog | None = None
    add_product_to_cart_quantity_value: int = 1

    edit_product_in_cart: dict | None = None


state = State()
