from nicegui import Client, ui

import components
from client import layout


@ui.page("/", title="Vendas")
def index(client: Client):
    client.on_connect(layout.render)

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Vendas")
