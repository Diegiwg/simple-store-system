from nicegui import ui
from nicegui.page import globals

import components
import routes
from styles import Typography


async def page():

    with ui.column().style(add="width: 100%; height: 95vh;") as element:
        globals.title = routes.route_manager.current_route.title
        components.page_title(routes.route_manager.current_route.title)

        wip = ui.label("00 MUITO TEXTO 11").classes(add="w-full")
        (
            Typography(wip)
            .font_size("6xl")
            .font_variant_numeric("oldstyle-nums")
            .font_weight("thin")
        )

    return element


sales_route = routes.Route("sales", "Vendas", page)
routes.route_manager.register_route(sales_route)
