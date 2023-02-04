from nicegui.ui import label, separator


def page_title(text: str):
    return (
        label(text).classes(add="text-2xl").style(add="align-self: center;"),
        separator(),
    )
