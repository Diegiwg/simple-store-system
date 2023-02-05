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


async def return_selected_item(table_id: int) -> int | None:
    selected_row = await get_selected_row(table_id)
    if len(selected_row) == 0:
        return None

    return int(selected_row[0]["id"])
