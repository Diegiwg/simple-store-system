from nicegui import app, ui

import api.routes  # Inicializar todas as rotas da API
import client.pages  # Inicializar todas as páginas do Cliente

app.add_static_files("/static", "static")
ui.run(dark=True)
