import json
from nicegui.ui import run_javascript


def default_col_def():
    return {
        "sortable": True,
        "filter": True,
        "floatingFilter": True,
    }


async def get_selected_row(table_id):
    data = await run_javascript(
        f"const id = (getElement({table_id}).gridOptions.api.getSelectedRows()); console.log('id', id); return JSON.stringify(id);"
    )
    return json.loads(data)
