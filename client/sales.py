import json
from nicegui import ui

from client import layout
import components
from javascript import fetch_api


async def get_data():
    message = await fetch_api("random/1000")
    ui.notify(json.dumps(message))


@ui.page("/", title="Vendas")
def index():
    layout.render()

    with ui.card().style(add="width: 100%; height: 95vh;"):
        components.page_title("Vendas")

        ui.button("Teste API retornando numeros aleatorios", on_click=get_data)
