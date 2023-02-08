from nicegui import Client, app, ui

import components
import pages
from routes import route_manager

route_manager.set_route("stock")


@ui.page("/")
async def render(client: Client):
    client.on_connect(components.render_layout)
    route_manager.set_root_element(ui.card().style(add="width: 100%; height: 95vh;"))
    await route_manager.run_route()


app.add_static_files("/static", "static")
ui.run(binding_refresh_interval=0.5)
