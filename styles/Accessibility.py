
from typing import Literal
from nicegui.element import Element
ScreenReaders = Literal["sr-only","not-sr-only"]
class Accessibility:
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

    def screen_readers(self, _readers: ScreenReaders):
        """
        Utilities for improving accessibility with screen readers.
        """
        self.__add(_readers)
        return self
        