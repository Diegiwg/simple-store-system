from nicegui import ui

import javascript


js_clock_code = """
function __python__UpdateClockData() {
    const clock_node = document.querySelector('.__python__clock-node')
    if (!clock_node) return

    const [date, time] = (new Date()).toLocaleString().split(' ')

    clock_node.querySelector('.__python__clock-date').textContent = date
    clock_node.querySelector('.__python__clock-time').textContent = time
}

setInterval(__python__UpdateClockData, 1);
"""


async def clock():
    with ui.card().classes(add="__python__clock-node").style(
        add="display: grid; justify-items: center; gap: 0;"
    ) as clock_node:
        ui.label("").classes(add="__python__clock-time").style(add="font-size: 2rem;")
        ui.label("").classes(add="__python__clock-date")

        await javascript.load_js(js_clock_code)
    return clock_node
