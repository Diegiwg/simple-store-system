from nicegui import ui

from style.page_title import ui_page_title


def menu_button(text: str, path: str):
    return ui.button(text, on_click=lambda: ui.open(path)).style(add="width: 100%;")


def globalLayout():
    ui.add_head_html(
        """
    <style>
        
    </style>
    """
    )

    with ui.left_drawer():
        with ui.column():
            with ui.row().style(
                add="display: flex; align-items: center; justify-content: center; width: 100%;"
            ):
                ui.image(source="/static/logo.png").props(add="width='50px'")
                ui.label("QUEIROZ LUBRIFICANTES").style(add="")
            ui.separator()
            menu_button("Vendas", "/")
            menu_button("Produtos", "/client/products")
            menu_button("Estoque", "/client/stock")
            ui.label("Label 4")
            ui.label("Label 5")
            ui.label("Label 6")
            ui.label("Label 7")
            ui.label("Label 8")
            ui.label("Label 9")
