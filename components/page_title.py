from nicegui.ui import label, separator


def page_title(text: str):
    return (
        label(text).classes(add="text-2xl text-center w-full"),
        separator(),
    )
