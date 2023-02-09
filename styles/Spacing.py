
from typing import Literal
from nicegui.element import Element
Padding = Literal["p-0","px-0","py-0","pt-0","pr-0","pb-0","pl-0","p-px","px-px","py-px","pt-px","pr-px","pb-px","pl-px","p-0.5","px-0.5","py-0.5","pt-0.5","pr-0.5","pb-0.5","pl-0.5","p-1","px-1","py-1","pt-1","pr-1","pb-1","pl-1","p-1.5","px-1.5","py-1.5","pt-1.5","pr-1.5","pb-1.5","pl-1.5","p-2","px-2","py-2","pt-2","pr-2","pb-2","pl-2","p-2.5","px-2.5","py-2.5","pt-2.5","pr-2.5","pb-2.5","pl-2.5","p-3","px-3","py-3","pt-3","pr-3","pb-3","pl-3","p-3.5","px-3.5","py-3.5","pt-3.5","pr-3.5","pb-3.5","pl-3.5","p-4","px-4","py-4","pt-4","pr-4","pb-4","pl-4","p-5","px-5","py-5","pt-5","pr-5","pb-5","pl-5","p-6","px-6","py-6","pt-6","pr-6","pb-6","pl-6","p-7","px-7","py-7","pt-7","pr-7","pb-7","pl-7","p-8","px-8","py-8","pt-8","pr-8","pb-8","pl-8","p-9","px-9","py-9","pt-9","pr-9","pb-9","pl-9","p-10","px-10","py-10","pt-10","pr-10","pb-10","pl-10","p-11","px-11","py-11","pt-11","pr-11","pb-11","pl-11","p-12","px-12","py-12","pt-12","pr-12","pb-12","pl-12","p-14","px-14","py-14","pt-14","pr-14","pb-14","pl-14","p-16","px-16","py-16","pt-16","pr-16","pb-16","pl-16","p-20","px-20","py-20","pt-20","pr-20","pb-20","pl-20","p-24","px-24","py-24","pt-24","pr-24","pb-24","pl-24","p-28","px-28","py-28","pt-28","pr-28","pb-28","pl-28","p-32","px-32","py-32","pt-32","pr-32","pb-32","pl-32","p-36","px-36","py-36","pt-36","pr-36","pb-36","pl-36","p-40","px-40","py-40","pt-40","pr-40","pb-40","pl-40","p-44","px-44","py-44","pt-44","pr-44","pb-44","pl-44","p-48","px-48","py-48","pt-48","pr-48","pb-48","pl-48","p-52","px-52","py-52","pt-52","pr-52","pb-52","pl-52","p-56","px-56","py-56","pt-56","pr-56","pb-56","pl-56","p-60","px-60","py-60","pt-60","pr-60","pb-60","pl-60","p-64","px-64","py-64","pt-64","pr-64","pb-64","pl-64","p-72","px-72","py-72","pt-72","pr-72","pb-72","pl-72","p-80","px-80","py-80","pt-80","pr-80","pb-80","pl-80","p-96","px-96","py-96","pt-96","pr-96","pb-96","pl-96"]

Margin = Literal["m-0","mx-0","my-0","mt-0","mr-0","mb-0","ml-0","m-px","mx-px","my-px","mt-px","mr-px","mb-px","ml-px","m-0.5","mx-0.5","my-0.5","mt-0.5","mr-0.5","mb-0.5","ml-0.5","m-1","mx-1","my-1","mt-1","mr-1","mb-1","ml-1","m-1.5","mx-1.5","my-1.5","mt-1.5","mr-1.5","mb-1.5","ml-1.5","m-2","mx-2","my-2","mt-2","mr-2","mb-2","ml-2","m-2.5","mx-2.5","my-2.5","mt-2.5","mr-2.5","mb-2.5","ml-2.5","m-3","mx-3","my-3","mt-3","mr-3","mb-3","ml-3","m-3.5","mx-3.5","my-3.5","mt-3.5","mr-3.5","mb-3.5","ml-3.5","m-4","mx-4","my-4","mt-4","mr-4","mb-4","ml-4","m-5","mx-5","my-5","mt-5","mr-5","mb-5","ml-5","m-6","mx-6","my-6","mt-6","mr-6","mb-6","ml-6","m-7","mx-7","my-7","mt-7","mr-7","mb-7","ml-7","m-8","mx-8","my-8","mt-8","mr-8","mb-8","ml-8","m-9","mx-9","my-9","mt-9","mr-9","mb-9","ml-9","m-10","mx-10","my-10","mt-10","mr-10","mb-10","ml-10","m-11","mx-11","my-11","mt-11","mr-11","mb-11","ml-11","m-12","mx-12","my-12","mt-12","mr-12","mb-12","ml-12","m-14","mx-14","my-14","mt-14","mr-14","mb-14","ml-14","m-16","mx-16","my-16","mt-16","mr-16","mb-16","ml-16","m-20","mx-20","my-20","mt-20","mr-20","mb-20","ml-20","m-24","mx-24","my-24","mt-24","mr-24","mb-24","ml-24","m-28","mx-28","my-28","mt-28","mr-28","mb-28","ml-28","m-32","mx-32","my-32","mt-32","mr-32","mb-32","ml-32","m-36","mx-36","my-36","mt-36","mr-36","mb-36","ml-36","m-40","mx-40","my-40","mt-40","mr-40","mb-40","ml-40","m-44","mx-44","my-44","mt-44","mr-44","mb-44","ml-44","m-48","mx-48","my-48","mt-48","mr-48","mb-48","ml-48","m-52","mx-52","my-52","mt-52","mr-52","mb-52","ml-52","m-56","mx-56","my-56","mt-56","mr-56","mb-56","ml-56","m-60","mx-60","my-60","mt-60","mr-60","mb-60","ml-60","m-64","mx-64","my-64","mt-64","mr-64","mb-64","ml-64","m-72","mx-72","my-72","mt-72","mr-72","mb-72","ml-72","m-80","mx-80","my-80","mt-80","mr-80","mb-80","ml-80","m-96","mx-96","my-96","mt-96","mr-96","mb-96","ml-96","m-auto","mx-auto","my-auto","mt-auto","mr-auto","mb-auto","ml-auto"]

SpaceBetween = Literal["space-x-0","space-y-0","space-x-0.5","space-y-0.5","space-x-1","space-y-1","space-x-1.5","space-y-1.5","space-x-2","space-y-2","space-x-2.5","space-y-2.5","space-x-3","space-y-3","space-x-3.5","space-y-3.5","space-x-4","space-y-4","space-x-5","space-y-5","space-x-6","space-y-6","space-x-7","space-y-7","space-x-8","space-y-8","space-x-9","space-y-9","space-x-10","space-y-10","space-x-11","space-y-11","space-x-12","space-y-12","space-x-14","space-y-14","space-x-16","space-y-16","space-x-20","space-y-20","space-x-24","space-y-24","space-x-28","space-y-28","space-x-32","space-y-32","space-x-36","space-y-36","space-x-40","space-y-40","space-x-44","space-y-44","space-x-48","space-y-48","space-x-52","space-y-52","space-x-56","space-y-56","space-x-60","space-y-60","space-x-64","space-y-64","space-x-72","space-y-72","space-x-80","space-y-80","space-x-96","space-y-96","space-x-px","space-y-px","space-y-reverse","space-x-reverse"]
class Spacing:
    def __init__(self, element: Element = Element("")) -> None:
        self.element = element
    def __add(self, _class: str) -> None:
        """
        Internal
        """
        self.element.classes(add=_class)
    def apply(self, ex_element: Element) -> Element:
        """
        Apply the Style to an outer element
        Args:
            ex_element (Element): External Element
        Returns:
            Element: External Element
        """
        return ex_element.classes(add=" ".join(self.element._classes))

    def padding(self, _padding: Padding):
        """
        Utilities for controlling an element's padding.
        """
        self.__add(_padding)
        return self
        

    def margin(self, _margin: Margin):
        """
        Utilities for controlling an element's margin.
        """
        self.__add(_margin)
        return self
        

    def space_between(self, _between: SpaceBetween):
        """
        Utilities for controlling the space between child elements.
        """
        self.__add(_between)
        return self
        