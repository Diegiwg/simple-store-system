
from typing import Literal
from nicegui.element import Element
TransitionProperty = Literal["transition-none","transition-all","transition","transition-colors","transition-opacity","transition-shadow","transition-transform"]

TransitionDuration = Literal["duration-75","duration-100","duration-150","duration-200","duration-300","duration-500","duration-700","duration-1000"]

TransitionTimingFunction = Literal["ease-linear","ease-in","ease-out","ease-in-out"]

TransitionDelay = Literal["delay-75","delay-100","delay-150","delay-200","delay-300","delay-500","delay-700","delay-1000"]

Animation = Literal["animate-none","animate-spin","animate-ping","animate-pulse","animate-bounce"]
class TransitionsAnimation:
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

    def transition_property(self, _property: TransitionProperty):
        """
        Utilities for controlling which CSS properties transition.
        """
        self.__add(_property)
        return self
        

    def transition_duration(self, _duration: TransitionDuration):
        """
        Utilities for controlling the duration of CSS transitions.
        """
        self.__add(_duration)
        return self
        

    def transition_timing_function(self, _function: TransitionTimingFunction):
        """
        Utilities for controlling the easing of CSS transitions.
        """
        self.__add(_function)
        return self
        

    def transition_delay(self, _delay: TransitionDelay):
        """
        Utilities for controlling the delay of CSS transitions.
        """
        self.__add(_delay)
        return self
        

    def animation(self, _animation: Animation):
        """
        Utilities for animating elements with CSS animations.
        """
        self.__add(_animation)
        return self
        