from nicegui import ui
from nicegui.page import globals

import components
from routes import Route, route_manager
from styles import Typography


async def page():

    with route_manager.root_element:
        globals.title = route_manager.current_route.title
        components.page_title(route_manager.current_route.title)

        wip = ui.label("00 MUITO TEXTO 11").classes(add="w-full")
        (
            Typography(wip)
            .font_size("6xl")
            .font_variant_numeric("oldstyle-nums")
            .font_weight("thin")
        )


sales_route = Route("sales", "Vendas", page)
route_manager.register_route(sales_route)
