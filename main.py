from nicegui import Client, app, ui

import components
import pages
import routes

routes.route_manager.set_route("sales")


@ui.page("/")
async def render(client: Client):
    with ui.card().style(add="width: 100%; height: 95vh;"):
        client.on_connect(components.render_layout)

        with ui.column().style(add="width: 100%; height: 95vh;") as root:
            element = await routes.route_manager.run_route()

        routes.state.root = root
        routes.state.element = element


app.add_static_files("/static", "static")
ui.run(binding_refresh_interval=0.5)
