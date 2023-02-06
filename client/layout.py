from nicegui import ui

from components import clock
from javascript import load_css

css_dark_table_theme_code = """
.ag-theme-balham {
    --ag-balham-active-color: #f5f5f5;
    --ag-foreground-color: #f5f5f5;
    --ag-background-color: #202020;
    --ag-header-background-color: #202020;
    --ag-subheader-background-color: #111;
    --ag-control-panel-background-color: #202020;
    --ag-border-color: #1a1c1d;
    --ag-odd-row-background-color: #202020;
    --ag-row-hover-color: #303030;
    --ag-column-hover-color: #1a1c1d;
    --ag-input-border-color: #f0f0f0;
    --ag-input-disabled-background-color: rgba(48, 46, 46, 0.3);
    --ag-modal-overlay-background-color: rgba(32, 32, 32, 0.66);
    --ag-checkbox-unchecked-color: #ecf0f1;
    --ag-secondary-foreground-color: var(--ag-foreground-color);
    /* --ag-disabled-foreground-color: hsla(0, 0%, 96.1%, 0.38); */
    --ag-subheader-toolbar-background-color: rgba(17, 17, 17, 0.5);
    --ag-row-border-color: #5c5c5c;
    --ag-chip-background-color: rgba(0, 0, 0, 0.08);
    --ag-range-selection-background-color: rgba(16, 16, 16, 0.2);
    --ag-range-selection-background-color-2: rgba(21, 21, 21, 0.36);
    --ag-range-selection-background-color-3: rgba(43, 43, 43, 0.49);
    --ag-range-selection-background-color-4: rgba(14, 14, 14, 0.59);
    --ag-selected-row-background-color: rgba(6, 9, 11, 0.28);
    --ag-header-column-separator-color: transparent;
    /* --ag-input-disabled-border-color: hsla(0, 0%, 94.1%, 0.3); */
    /* --ag-header-foreground-color: hsla(0, 0%, 96.1%, 0.64); */
    --ag-toggle-button-off-background-color: transparent;
    --ag-toggle-button-off-border-color: var(--ag-foreground-color);
    --ag-range-selection-chart-category-background-color: #1a1c1d;
    --ag-range-selection-chart-background-color: rgba(34, 34, 34, 0.5);
}
"""


def menu_button(text: str, path: str):
    return ui.button(text, on_click=lambda: ui.open(path)).style(add="width: 100%;")


async def render():

    with ui.left_drawer():
        with ui.column():
            with ui.row().style(
                add="display: flex; align-items: center; justify-content: center; width: 100%;"
            ):
                ui.image(source="/static/logo.png").props(add="width='50px'")
                ui.label("QUEIROZ LUBRIFICANTES").style(add="")
            ui.separator()

            with ui.column().style(
                add="width: 100%; height: 85vh; display: grid; align-content: space-between;"
            ):
                with ui.column().style(add="width: 100%;"):
                    menu_button("Vendas", "/")
                    menu_button("Produtos", "/client/products")
                    menu_button("Estoque", "/client/stock")

                await clock()
                # await load_css(css_dark_table_theme_code)
