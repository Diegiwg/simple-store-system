from nicegui import Client, ui

import components


@ui.page("/", title="Vendas")
def render(client: Client):
    client.on_connect(components.render_layout)

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Vendas")
