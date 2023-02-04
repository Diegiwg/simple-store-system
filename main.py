from nicegui import ui, app
from client.global_layout import globalLayout
from style.page_title import ui_page_title

import api.routes  # Inicializar todas as rotas da API
import client.pages  # Inicializar todas as páginas do Cliente


app.add_static_files("/static", "static")
ui.run(dark=True)
