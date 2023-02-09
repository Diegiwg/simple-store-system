from nicegui import ui

import javascript
from styles import Typography

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

        (
            Typography(ui.label(""))
            .font_family("font-mono")
            .font_size("text-4xl")
            .font_weight("font-bold")
            .text_color("text-neutral-700")
            .font_smoothing("antialiased")
            .element
        ).classes(add="__python__clock-time")

        (
            Typography(ui.label(""))
            .font_family("font-mono")
            .font_size("text-lg")
            .font_weight("font-medium")
            .text_color("text-neutral-500")
            .element
        ).classes(add="__python__clock-date")

        await javascript.load_js(js_clock_code)

    return clock_node
