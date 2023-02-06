import json

from nicegui.ui import run_javascript


def default_col_def():
    return {
        "sortable": True,
        "filter": True,
        "floatingFilter": True,
    }


async def call_api_function(table_id, function_name):
    data: str = (
        await run_javascript(
            f"return JSON.stringify(getElement({table_id}).gridOptions.api.{function_name}());"
        )
        or "[]"
    )
    return json.loads(data)


async def get_selected_rows(table_id: int) -> int | None:
    selected_row = await call_api_function(table_id, "getSelectedRows")

    if len(selected_row) == 0:
        return None

    return int(selected_row[0]["id"])
