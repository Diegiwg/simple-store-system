import json

from nicegui.ui import run_javascript


def default_col_def():
    return {
        "sortable": True,
        "filter": True,
        "floatingFilter": True,
    }


async def get_selected_row(table_id):
    data: str = (
        await run_javascript(
            f"return JSON.stringify(getElement({table_id}).gridOptions.api.getSelectedRows());"
        )
        or "[]"
    )
    return json.loads(data)
