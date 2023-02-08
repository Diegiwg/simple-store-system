from dataclasses import dataclass
from typing import Callable

from nicegui.element import Element


@dataclass
class Route:
    path: str
    title: str
    handler: Callable


class RouteManager:
    routes: dict[str, Route]
    current_route: Route

    def __init__(self) -> None:
        self.routes = dict()

    def register_route(self, route: Route):
        self.routes[route.path] = route

    def set_route(self, route_path: str):
        self.current_route = self.routes[route_path]

    async def run_route(self):
        return await self.current_route.handler()


route_manager = RouteManager()


@dataclass
class State:
    root: Element
    element: Element


state = State(root=Element(""), element=Element(""))


@dataclass
class Redirect:
    route_path: str

    async def run(self):
        route_manager.set_route(self.route_path)
        temp: Element = await route_manager.run_route()

        state.element.clear()
        state.element.slots = temp.slots
        state.root.remove(temp)

        state.element.style(add="width: 100%; height: 95vh;")
