from nicegui import ui

from components import clock
from routes import Navigator
from styles import Typography


def menu_button(text: str, path: str):
    return (
        Typography(
            ui.button(text, on_click=Navigator(path).redirect).style(add="width: 100%;")
        )
        .text_align("text-center")
        .font_weight("font-bold")
        .element
    )


async def render():
    with ui.left_drawer():
        with ui.column():
            with ui.row().style(
                add="display: flex; align-items: center; justify-content: center; width: 100%;"
            ):
                ui.image(source="/static/logo.png").props(add="width='50px'")
                (
                    Typography(ui.label("QUEIROZ LUBRIFICANTES"))
                    .font_family("font-mono")
                    .font_weight("font-light")
                    .element
                )
            ui.separator()

            with ui.column().style(
                add="width: 100%; height: 85vh; display: grid; align-content: space-between;"
            ):
                with ui.column().style(add="width: 100%;"):
                    menu_button("Vendas", "sales")
                    menu_button("Produtos", "products")
                    menu_button("Estoque", "stock")

                await clock()
