from nicegui import ui
from nicegui.page import globals

import components
import routes


async def page():

    with ui.column().style(add="width: 100%; height: 95vh;") as element:
        globals.title = routes.route_manager.current_route.title
        components.page_title(routes.route_manager.current_route.title)

        ui.label("WIP").classes(add="text-center w-full")

    return element


sales_route = routes.Route("sales", "Vendas", page)
routes.route_manager.register_route(sales_route)
