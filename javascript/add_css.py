from nicegui.ui import run_javascript

import javascript


async def add_css(css_file_name: str):
    javascript_source = await javascript.fetch("/static/code/add_css.js")
    await run_javascript(
        code=f"const css_file_name='{css_file_name}'; {javascript_source}",
        respond=False,
    )
