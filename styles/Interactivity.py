
from typing import Literal
from nicegui.element import Element
AccentColor = Literal["accent-inherit","accent-current","accent-transparent","accent-black","accent-white","accent-slate-50","accent-slate-100","accent-slate-200","accent-slate-300","accent-slate-400","accent-slate-500","accent-slate-600","accent-slate-700","accent-slate-800","accent-slate-900","accent-gray-50","accent-gray-100","accent-gray-200","accent-gray-300","accent-gray-400","accent-gray-500","accent-gray-600","accent-gray-700","accent-gray-800","accent-gray-900","accent-zinc-50","accent-zinc-100","accent-zinc-200","accent-zinc-300","accent-zinc-400","accent-zinc-500","accent-zinc-600","accent-zinc-700","accent-zinc-800","accent-zinc-900","accent-neutral-50","accent-neutral-100","accent-neutral-200","accent-neutral-300","accent-neutral-400","accent-neutral-500","accent-neutral-600","accent-neutral-700","accent-neutral-800","accent-neutral-900","accent-stone-50","accent-stone-100","accent-stone-200","accent-stone-300","accent-stone-400","accent-stone-500","accent-stone-600","accent-stone-700","accent-stone-800","accent-stone-900","accent-red-50","accent-red-100","accent-red-200","accent-red-300","accent-red-400","accent-red-500","accent-red-600","accent-red-700","accent-red-800","accent-red-900","accent-orange-50","accent-orange-100","accent-orange-200","accent-orange-300","accent-orange-400","accent-orange-500","accent-orange-600","accent-orange-700","accent-orange-800","accent-orange-900","accent-amber-50","accent-amber-100","accent-amber-200","accent-amber-300","accent-amber-400","accent-amber-500","accent-amber-600","accent-amber-700","accent-amber-800","accent-amber-900","accent-yellow-50","accent-yellow-100","accent-yellow-200","accent-yellow-300","accent-yellow-400","accent-yellow-500","accent-yellow-600","accent-yellow-700","accent-yellow-800","accent-yellow-900","accent-lime-50","accent-lime-100","accent-lime-200","accent-lime-300","accent-lime-400","accent-lime-500","accent-lime-600","accent-lime-700","accent-lime-800","accent-lime-900","accent-green-50","accent-green-100","accent-green-200","accent-green-300","accent-green-400","accent-green-500","accent-green-600","accent-green-700","accent-green-800","accent-green-900","accent-emerald-50","accent-emerald-100","accent-emerald-200","accent-emerald-300","accent-emerald-400","accent-emerald-500","accent-emerald-600","accent-emerald-700","accent-emerald-800","accent-emerald-900","accent-teal-50","accent-teal-100","accent-teal-200","accent-teal-300","accent-teal-400","accent-teal-500","accent-teal-600","accent-teal-700","accent-teal-800","accent-teal-900","accent-cyan-50","accent-cyan-100","accent-cyan-200","accent-cyan-300","accent-cyan-400","accent-cyan-500","accent-cyan-600","accent-cyan-700","accent-cyan-800","accent-cyan-900","accent-sky-50","accent-sky-100","accent-sky-200","accent-sky-300","accent-sky-400","accent-sky-500","accent-sky-600","accent-sky-700","accent-sky-800","accent-sky-900","accent-blue-50","accent-blue-100","accent-blue-200","accent-blue-300","accent-blue-400","accent-blue-500","accent-blue-600","accent-blue-700","accent-blue-800","accent-blue-900","accent-indigo-50","accent-indigo-100","accent-indigo-200","accent-indigo-300","accent-indigo-400","accent-indigo-500","accent-indigo-600","accent-indigo-700","accent-indigo-800","accent-indigo-900","accent-violet-50","accent-violet-100","accent-violet-200","accent-violet-300","accent-violet-400","accent-violet-500","accent-violet-600","accent-violet-700","accent-violet-800","accent-violet-900","accent-purple-50","accent-purple-100","accent-purple-200","accent-purple-300","accent-purple-400","accent-purple-500","accent-purple-600","accent-purple-700","accent-purple-800","accent-purple-900","accent-fuchsia-50","accent-fuchsia-100","accent-fuchsia-200","accent-fuchsia-300","accent-fuchsia-400","accent-fuchsia-500","accent-fuchsia-600","accent-fuchsia-700","accent-fuchsia-800","accent-fuchsia-900","accent-pink-50","accent-pink-100","accent-pink-200","accent-pink-300","accent-pink-400","accent-pink-500","accent-pink-600","accent-pink-700","accent-pink-800","accent-pink-900","accent-rose-50","accent-rose-100","accent-rose-200","accent-rose-300","accent-rose-400","accent-rose-500","accent-rose-600","accent-rose-700","accent-rose-800","accent-rose-900","accent-auto"]

Appearance = Literal["appearance-none"]

Cursor = Literal["cursor-auto","cursor-default","cursor-pointer","cursor-wait","cursor-text","cursor-move","cursor-help","cursor-not-allowed","cursor-none","cursor-context-menu","cursor-progress","cursor-cell","cursor-crosshair","cursor-vertical-text","cursor-alias","cursor-copy","cursor-no-drop","cursor-grab","cursor-grabbing","cursor-all-scroll","cursor-col-resize","cursor-row-resize","cursor-n-resize","cursor-e-resize","cursor-s-resize","cursor-w-resize","cursor-ne-resize","cursor-nw-resize","cursor-se-resize","cursor-sw-resize","cursor-ew-resize","cursor-ns-resize","cursor-nesw-resize","cursor-nwse-resize","cursor-zoom-in","cursor-zoom-out"]

CaretColor = Literal["caret-inherit","caret-current","caret-transparent","caret-black","caret-white","caret-slate-50","caret-slate-100","caret-slate-200","caret-slate-300","caret-slate-400","caret-slate-500","caret-slate-600","caret-slate-700","caret-slate-800","caret-slate-900","caret-gray-50","caret-gray-100","caret-gray-200","caret-gray-300","caret-gray-400","caret-gray-500","caret-gray-600","caret-gray-700","caret-gray-800","caret-gray-900","caret-zinc-50","caret-zinc-100","caret-zinc-200","caret-zinc-300","caret-zinc-400","caret-zinc-500","caret-zinc-600","caret-zinc-700","caret-zinc-800","caret-zinc-900","caret-neutral-50","caret-neutral-100","caret-neutral-200","caret-neutral-300","caret-neutral-400","caret-neutral-500","caret-neutral-600","caret-neutral-700","caret-neutral-800","caret-neutral-900","caret-stone-50","caret-stone-100","caret-stone-200","caret-stone-300","caret-stone-400","caret-stone-500","caret-stone-600","caret-stone-700","caret-stone-800","caret-stone-900","caret-red-50","caret-red-100","caret-red-200","caret-red-300","caret-red-400","caret-red-500","caret-red-600","caret-red-700","caret-red-800","caret-red-900","caret-orange-50","caret-orange-100","caret-orange-200","caret-orange-300","caret-orange-400","caret-orange-500","caret-orange-600","caret-orange-700","caret-orange-800","caret-orange-900","caret-amber-50","caret-amber-100","caret-amber-200","caret-amber-300","caret-amber-400","caret-amber-500","caret-amber-600","caret-amber-700","caret-amber-800","caret-amber-900","caret-yellow-50","caret-yellow-100","caret-yellow-200","caret-yellow-300","caret-yellow-400","caret-yellow-500","caret-yellow-600","caret-yellow-700","caret-yellow-800","caret-yellow-900","caret-lime-50","caret-lime-100","caret-lime-200","caret-lime-300","caret-lime-400","caret-lime-500","caret-lime-600","caret-lime-700","caret-lime-800","caret-lime-900","caret-green-50","caret-green-100","caret-green-200","caret-green-300","caret-green-400","caret-green-500","caret-green-600","caret-green-700","caret-green-800","caret-green-900","caret-emerald-50","caret-emerald-100","caret-emerald-200","caret-emerald-300","caret-emerald-400","caret-emerald-500","caret-emerald-600","caret-emerald-700","caret-emerald-800","caret-emerald-900","caret-teal-50","caret-teal-100","caret-teal-200","caret-teal-300","caret-teal-400","caret-teal-500","caret-teal-600","caret-teal-700","caret-teal-800","caret-teal-900","caret-cyan-50","caret-cyan-100","caret-cyan-200","caret-cyan-300","caret-cyan-400","caret-cyan-500","caret-cyan-600","caret-cyan-700","caret-cyan-800","caret-cyan-900","caret-sky-50","caret-sky-100","caret-sky-200","caret-sky-300","caret-sky-400","caret-sky-500","caret-sky-600","caret-sky-700","caret-sky-800","caret-sky-900","caret-blue-50","caret-blue-100","caret-blue-200","caret-blue-300","caret-blue-400","caret-blue-500","caret-blue-600","caret-blue-700","caret-blue-800","caret-blue-900","caret-indigo-50","caret-indigo-100","caret-indigo-200","caret-indigo-300","caret-indigo-400","caret-indigo-500","caret-indigo-600","caret-indigo-700","caret-indigo-800","caret-indigo-900","caret-violet-50","caret-violet-100","caret-violet-200","caret-violet-300","caret-violet-400","caret-violet-500","caret-violet-600","caret-violet-700","caret-violet-800","caret-violet-900","caret-purple-50","caret-purple-100","caret-purple-200","caret-purple-300","caret-purple-400","caret-purple-500","caret-purple-600","caret-purple-700","caret-purple-800","caret-purple-900","caret-fuchsia-50","caret-fuchsia-100","caret-fuchsia-200","caret-fuchsia-300","caret-fuchsia-400","caret-fuchsia-500","caret-fuchsia-600","caret-fuchsia-700","caret-fuchsia-800","caret-fuchsia-900","caret-pink-50","caret-pink-100","caret-pink-200","caret-pink-300","caret-pink-400","caret-pink-500","caret-pink-600","caret-pink-700","caret-pink-800","caret-pink-900","caret-rose-50","caret-rose-100","caret-rose-200","caret-rose-300","caret-rose-400","caret-rose-500","caret-rose-600","caret-rose-700","caret-rose-800","caret-rose-900"]

PointerEvents = Literal["pointer-events-none","pointer-events-auto"]

Resize = Literal["resize-none","resize-y","resize-x","resize"]

ScrollBehavior = Literal["scroll-auto","scroll-smooth"]

ScrollMargin = Literal["scroll-m-0","scroll-mx-0","scroll-my-0","scroll-mt-0","scroll-mr-0","scroll-mb-0","scroll-ml-0","scroll-m-px","scroll-mx-px","scroll-my-px","scroll-mt-px","scroll-mr-px","scroll-mb-px","scroll-ml-px","scroll-m-0.5","scroll-mx-0.5","scroll-my-0.5","scroll-mt-0.5","scroll-mr-0.5","scroll-mb-0.5","scroll-ml-0.5","scroll-m-1","scroll-mx-1","scroll-my-1","scroll-mt-1","scroll-mr-1","scroll-mb-1","scroll-ml-1","scroll-m-1.5","scroll-mx-1.5","scroll-my-1.5","scroll-mt-1.5","scroll-mr-1.5","scroll-mb-1.5","scroll-ml-1.5","scroll-m-2","scroll-mx-2","scroll-my-2","scroll-mt-2","scroll-mr-2","scroll-mb-2","scroll-ml-2","scroll-m-2.5","scroll-mx-2.5","scroll-my-2.5","scroll-mt-2.5","scroll-mr-2.5","scroll-mb-2.5","scroll-ml-2.5","scroll-m-3","scroll-mx-3","scroll-my-3","scroll-mt-3","scroll-mr-3","scroll-mb-3","scroll-ml-3","scroll-m-3.5","scroll-mx-3.5","scroll-my-3.5","scroll-mt-3.5","scroll-mr-3.5","scroll-mb-3.5","scroll-ml-3.5","scroll-m-4","scroll-mx-4","scroll-my-4","scroll-mt-4","scroll-mr-4","scroll-mb-4","scroll-ml-4","scroll-m-5","scroll-mx-5","scroll-my-5","scroll-mt-5","scroll-mr-5","scroll-mb-5","scroll-ml-5","scroll-m-6","scroll-mx-6","scroll-my-6","scroll-mt-6","scroll-mr-6","scroll-mb-6","scroll-ml-6","scroll-m-7","scroll-mx-7","scroll-my-7","scroll-mt-7","scroll-mr-7","scroll-mb-7","scroll-ml-7","scroll-m-8","scroll-mx-8","scroll-my-8","scroll-mt-8","scroll-mr-8","scroll-mb-8","scroll-ml-8","scroll-m-9","scroll-mx-9","scroll-my-9","scroll-mt-9","scroll-mr-9","scroll-mb-9","scroll-ml-9","scroll-m-10","scroll-mx-10","scroll-my-10","scroll-mt-10","scroll-mr-10","scroll-mb-10","scroll-ml-10","scroll-m-11","scroll-mx-11","scroll-my-11","scroll-mt-11","scroll-mr-11","scroll-mb-11","scroll-ml-11","scroll-m-12","scroll-mx-12","scroll-my-12","scroll-mt-12","scroll-mr-12","scroll-mb-12","scroll-ml-12","scroll-m-14","scroll-mx-14","scroll-my-14","scroll-mt-14","scroll-mr-14","scroll-mb-14","scroll-ml-14","scroll-m-16","scroll-mx-16","scroll-my-16","scroll-mt-16","scroll-mr-16","scroll-mb-16","scroll-ml-16","scroll-m-20","scroll-mx-20","scroll-my-20","scroll-mt-20","scroll-mr-20","scroll-mb-20","scroll-ml-20","scroll-m-24","scroll-mx-24","scroll-my-24","scroll-mt-24","scroll-mr-24","scroll-mb-24","scroll-ml-24","scroll-m-28","scroll-mx-28","scroll-my-28","scroll-mt-28","scroll-mr-28","scroll-mb-28","scroll-ml-28","scroll-m-32","scroll-mx-32","scroll-my-32","scroll-mt-32","scroll-mr-32","scroll-mb-32","scroll-ml-32","scroll-m-36","scroll-mx-36","scroll-my-36","scroll-mt-36","scroll-mr-36","scroll-mb-36","scroll-ml-36","scroll-m-40","scroll-mx-40","scroll-my-40","scroll-mt-40","scroll-mr-40","scroll-mb-40","scroll-ml-40","scroll-m-44","scroll-mx-44","scroll-my-44","scroll-mt-44","scroll-mr-44","scroll-mb-44","scroll-ml-44","scroll-m-48","scroll-mx-48","scroll-my-48","scroll-mt-48","scroll-mr-48","scroll-mb-48","scroll-ml-48","scroll-m-52","scroll-mx-52","scroll-my-52","scroll-mt-52","scroll-mr-52","scroll-mb-52","scroll-ml-52","scroll-m-56","scroll-mx-56","scroll-my-56","scroll-mt-56","scroll-mr-56","scroll-mb-56","scroll-ml-56","scroll-m-60","scroll-mx-60","scroll-my-60","scroll-mt-60","scroll-mr-60","scroll-mb-60","scroll-ml-60","scroll-m-64","scroll-mx-64","scroll-my-64","scroll-mt-64","scroll-mr-64","scroll-mb-64","scroll-ml-64","scroll-m-72","scroll-mx-72","scroll-my-72","scroll-mt-72","scroll-mr-72","scroll-mb-72","scroll-ml-72","scroll-m-80","scroll-mx-80","scroll-my-80","scroll-mt-80","scroll-mr-80","scroll-mb-80","scroll-ml-80","scroll-m-96","scroll-mx-96","scroll-my-96","scroll-mt-96","scroll-mr-96","scroll-mb-96","scroll-ml-96"]

ScrollPadding = Literal["scroll-p-0","scroll-px-0","scroll-py-0","scroll-pt-0","scroll-pr-0","scroll-pb-0","scroll-pl-0","scroll-p-px","scroll-px-px","scroll-py-px","scroll-pt-px","scroll-pr-px","scroll-pb-px","scroll-pl-px","scroll-p-0.5","scroll-px-0.5","scroll-py-0.5","scroll-pt-0.5","scroll-pr-0.5","scroll-pb-0.5","scroll-pl-0.5","scroll-p-1","scroll-px-1","scroll-py-1","scroll-pt-1","scroll-pr-1","scroll-pb-1","scroll-pl-1","scroll-p-1.5","scroll-px-1.5","scroll-py-1.5","scroll-pt-1.5","scroll-pr-1.5","scroll-pb-1.5","scroll-pl-1.5","scroll-p-2","scroll-px-2","scroll-py-2","scroll-pt-2","scroll-pr-2","scroll-pb-2","scroll-pl-2","scroll-p-2.5","scroll-px-2.5","scroll-py-2.5","scroll-pt-2.5","scroll-pr-2.5","scroll-pb-2.5","scroll-pl-2.5","scroll-p-3","scroll-px-3","scroll-py-3","scroll-pt-3","scroll-pr-3","scroll-pb-3","scroll-pl-3","scroll-p-3.5","scroll-px-3.5","scroll-py-3.5","scroll-pt-3.5","scroll-pr-3.5","scroll-pb-3.5","scroll-pl-3.5","scroll-p-4","scroll-px-4","scroll-py-4","scroll-pt-4","scroll-pr-4","scroll-pb-4","scroll-pl-4","scroll-p-5","scroll-px-5","scroll-py-5","scroll-pt-5","scroll-pr-5","scroll-pb-5","scroll-pl-5","scroll-p-6","scroll-px-6","scroll-py-6","scroll-pt-6","scroll-pr-6","scroll-pb-6","scroll-pl-6","scroll-p-7","scroll-px-7","scroll-py-7","scroll-pt-7","scroll-pr-7","scroll-pb-7","scroll-pl-7","scroll-p-8","scroll-px-8","scroll-py-8","scroll-pt-8","scroll-pr-8","scroll-pb-8","scroll-pl-8","scroll-p-9","scroll-px-9","scroll-py-9","scroll-pt-9","scroll-pr-9","scroll-pb-9","scroll-pl-9","scroll-p-10","scroll-px-10","scroll-py-10","scroll-pt-10","scroll-pr-10","scroll-pb-10","scroll-pl-10","scroll-p-11","scroll-px-11","scroll-py-11","scroll-pt-11","scroll-pr-11","scroll-pb-11","scroll-pl-11","scroll-p-12","scroll-px-12","scroll-py-12","scroll-pt-12","scroll-pr-12","scroll-pb-12","scroll-pl-12","scroll-p-14","scroll-px-14","scroll-py-14","scroll-pt-14","scroll-pr-14","scroll-pb-14","scroll-pl-14","scroll-p-16","scroll-px-16","scroll-py-16","scroll-pt-16","scroll-pr-16","scroll-pb-16","scroll-pl-16","scroll-p-20","scroll-px-20","scroll-py-20","scroll-pt-20","scroll-pr-20","scroll-pb-20","scroll-pl-20","scroll-p-24","scroll-px-24","scroll-py-24","scroll-pt-24","scroll-pr-24","scroll-pb-24","scroll-pl-24","scroll-p-28","scroll-px-28","scroll-py-28","scroll-pt-28","scroll-pr-28","scroll-pb-28","scroll-pl-28","scroll-p-32","scroll-px-32","scroll-py-32","scroll-pt-32","scroll-pr-32","scroll-pb-32","scroll-pl-32","scroll-p-36","scroll-px-36","scroll-py-36","scroll-pt-36","scroll-pr-36","scroll-pb-36","scroll-pl-36","scroll-p-40","scroll-px-40","scroll-py-40","scroll-pt-40","scroll-pr-40","scroll-pb-40","scroll-pl-40","scroll-p-44","scroll-px-44","scroll-py-44","scroll-pt-44","scroll-pr-44","scroll-pb-44","scroll-pl-44","scroll-p-48","scroll-px-48","scroll-py-48","scroll-pt-48","scroll-pr-48","scroll-pb-48","scroll-pl-48","scroll-p-52","scroll-px-52","scroll-py-52","scroll-pt-52","scroll-pr-52","scroll-pb-52","scroll-pl-52","scroll-p-56","scroll-px-56","scroll-py-56","scroll-pt-56","scroll-pr-56","scroll-pb-56","scroll-pl-56","scroll-p-60","scroll-px-60","scroll-py-60","scroll-pt-60","scroll-pr-60","scroll-pb-60","scroll-pl-60","scroll-p-64","scroll-px-64","scroll-py-64","scroll-pt-64","scroll-pr-64","scroll-pb-64","scroll-pl-64","scroll-p-72","scroll-px-72","scroll-py-72","scroll-pt-72","scroll-pr-72","scroll-pb-72","scroll-pl-72","scroll-p-80","scroll-px-80","scroll-py-80","scroll-pt-80","scroll-pr-80","scroll-pb-80","scroll-pl-80","scroll-p-96","scroll-px-96","scroll-py-96","scroll-pt-96","scroll-pr-96","scroll-pb-96","scroll-pl-96"]

ScrollSnapAlign = Literal["snap-start","snap-end","snap-center","snap-align-none"]

ScrollSnapStop = Literal["snap-normal","snap-always"]

ScrollSnapType = Literal["snap-none","snap-x","snap-y","snap-both","snap-mandatory","snap-proximity"]

TouchAction = Literal["touch-auto","touch-none","touch-pan-x","touch-pan-left","touch-pan-right","touch-pan-y","touch-pan-up","touch-pan-down","touch-pinch-zoom","touch-manipulation"]

UserSelect = Literal["select-none","select-text","select-all","select-auto"]

WillChange = Literal["will-change-auto","will-change-scroll","will-change-contents","will-change-transform"]
class Interactivity:
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

    def accent_color(self, _color: AccentColor):
        """
        Utilities for controlling the accented color of a form control.
        """
        self.__add(_color)
        return self
        

    def appearance(self, _appearance: Appearance):
        """
        Utilities for suppressing native form control styling.
        """
        self.__add(_appearance)
        return self
        

    def cursor(self, _cursor: Cursor):
        """
        Utilities for controlling the cursor style when hovering over an element.
        """
        self.__add(_cursor)
        return self
        

    def caret_color(self, _color: CaretColor):
        """
        Utilities for controlling the color of the text input cursor.
        """
        self.__add(_color)
        return self
        

    def pointer_events(self, _events: PointerEvents):
        """
        Utilities for controlling whether an element responds to pointer events.
        """
        self.__add(_events)
        return self
        

    def resize(self, _resize: Resize):
        """
        Utilities for controlling how an element can be resized.
        """
        self.__add(_resize)
        return self
        

    def scroll_behavior(self, _behavior: ScrollBehavior):
        """
        Utilities for controlling the scroll behavior of an element.
        """
        self.__add(_behavior)
        return self
        

    def scroll_margin(self, _margin: ScrollMargin):
        """
        Utilities for controlling the scroll offset around items in a snap container.
        """
        self.__add(_margin)
        return self
        

    def scroll_padding(self, _padding: ScrollPadding):
        """
        Utilities for controlling an element's scroll offset within a snap container.
        """
        self.__add(_padding)
        return self
        

    def scroll_snap_align(self, _align: ScrollSnapAlign):
        """
        Utilities for controlling the scroll snap alignment of an element.
        """
        self.__add(_align)
        return self
        

    def scroll_snap_stop(self, _stop: ScrollSnapStop):
        """
        Utilities for controlling whether you can skip past possible snap positions.
        """
        self.__add(_stop)
        return self
        

    def scroll_snap_type(self, _type: ScrollSnapType):
        """
        Utilities for controlling how strictly snap points are enforced in a snap container.
        """
        self.__add(_type)
        return self
        

    def touch_action(self, _action: TouchAction):
        """
        Utilities for controlling how an element can be scrolled and zoomed on touchscreens.
        """
        self.__add(_action)
        return self
        

    def user_select(self, _select: UserSelect):
        """
        Utilities for controlling whether the user can select text in an element.
        """
        self.__add(_select)
        return self
        

    def will_change(self, _change: WillChange):
        """
        Utilities for optimizing upcoming animations of elements that are expected to change.
        """
        self.__add(_change)
        return self
        