from typing import Callable

from nicegui.element import Element


class Route:
    path: str
    title: str
    handler: Callable

    def __init__(self, path: str, title: str, handler: Callable):
        self.path = path
        self.title = title
        self.handler = handler


class RouteManager:
    routes: dict[str, Route]
    current_route: Route
    root_element: Element

    def __init__(self) -> None:
        self.routes = dict()

    def set_root_element(self, element: Element) -> None:
        self.root_element = element

    def register_route(self, route: Route):
        self.routes[route.path] = route

    def set_route(self, route_path: str):
        self.current_route = self.routes[route_path]

    async def run_route(self):
        return await self.current_route.handler()


route_manager = RouteManager()


class Navigator:
    route_path: str

    def __init__(self, route_path: str):
        self.route_path = route_path

    async def redirect(self):
        route_manager.set_route(self.route_path)
        route_manager.root_element.clear()
        return await route_manager.run_route()
