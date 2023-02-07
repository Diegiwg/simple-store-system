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
        time = ui.label("").classes(
            add="__python__clock-time"
        )  # .style(add="font-size: 2rem;")
        date = ui.label("").classes(add="__python__clock-date")

        await javascript.load_js(js_clock_code)

        Typography(time).font_family("mono").font_size("4xl").font_weight(
            "bold"
        ).text_color("neutral-700").font_smoothing("antialiased")

        Typography(date).font_family("mono").font_size("lg").font_weight(
            "medium"
        ).text_color("neutral-500")

    return clock_node
