import json
from nicegui import ui

from client.global_layout import globalLayout
from javascript.fetch_api import fetch_api
from style.page_title import ui_page_title


async def get_data():
    message = await fetch_api("random/1000")
    ui.notify(json.dumps(message))


@ui.page("/", title="Vendas")
def index():
    globalLayout()
    with ui.card().style(add="width: 100%; height: 95vh;"):
        ui_page_title("Vendas")

        ui.button("AA", on_click=get_data)
