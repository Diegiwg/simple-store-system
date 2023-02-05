from nicegui import ui

from components import clock
from javascript import add_css


def menu_button(text: str, path: str):
    return ui.button(text, on_click=lambda: ui.open(path)).style(add="width: 100%;")


async def render():

    with ui.left_drawer():
        with ui.column():
            with ui.row().style(
                add="display: flex; align-items: center; justify-content: center; width: 100%;"
            ):
                ui.image(source="/static/logo.png").props(add="width='50px'")
                ui.label("QUEIROZ LUBRIFICANTES").style(add="")
            ui.separator()

            with ui.column().style(
                add="width: 100%; height: 85vh; display: grid; align-content: space-between;"
            ):
                with ui.column().style(add="width: 100%;"):
                    menu_button("Vendas", "/")
                    menu_button("Produtos", "/client/products")
                    menu_button("Estoque", "/client/stock")

                await clock()
                await add_css("ag-table-dark")
