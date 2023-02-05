from nicegui import ui

import javascript


async def js_clock():
    source = await javascript.fetch("/static/code/clock.js") or ""
    await ui.run_javascript(code=source, respond=False)


async def clock():
    with ui.card().classes(add="__python__clock-node").style(
        add="display: grid; justify-items: center; gap: 0;"
    ) as c:
        ui.label("").classes(add="__python__clock-time").style(add="font-size: 2rem;")
        ui.label("").classes(add="__python__clock-date")

        await js_clock()
    return c
