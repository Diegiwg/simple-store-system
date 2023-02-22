from nicegui import ui

import styles

from .state import state


def generator_form_input(name: str, prop: str):
    el_input = ui.input(f"{name}: {state.edit_product_in_cart[prop]}")
    el_input._props["disable"] = True
    return styles.Sizing(el_input).width("w-full").element


async def edit_product_in_cart():
    with ui.dialog() as dialog, styles.Sizing(ui.card()).width("w-full").element:
        ui.label("Editar Produto no Carrinho")

        state.edit_product_in_cart = await state.current_cart_table.get_selected_row()
        if state.edit_product_in_cart is None:
            return

        generator_form_input("Nome", "name")
        generator_form_input("Marca", "brand")
        generator_form_input("Referencia", "reference")
        generator_form_input("Preço", "price")

        with ui.row() as el:
            styles.Sizing(el).width("w-full")
            styles.FlexboxGrid(el).align_items("items-center").justify_content(
                "justify-between"
            )

            ui.number("Quantidade")
            ui.button("Salvar")

    dialog.open()
