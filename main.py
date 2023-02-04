from nicegui import app, ui

import api.routes as routes
import client.pages as pages

app.add_static_files("/static", "static")
ui.run(dark=True, binding_refresh_interval=0.5)
