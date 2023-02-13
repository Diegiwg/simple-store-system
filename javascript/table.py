import json

from nicegui.ui import run_javascript


async def call_api_function(table_id, function_name):
    data: str = (
        await run_javascript(
            f"return JSON.stringify(getElement({table_id}).gridOptions.api.{function_name}());"
        )
        or "[]"
    )
    return json.loads(data)


async def get_selected_row(table_id: int):
    selected_row = await call_api_function(table_id, "getSelectedRows")

    if len(selected_row) == 0:
        return None

    return selected_row[0]
