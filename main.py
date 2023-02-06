from nicegui import app, ui

import pages

app.add_static_files("/static", "static")
ui.run(binding_refresh_interval=0.5)
