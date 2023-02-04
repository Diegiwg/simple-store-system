from nicegui.ui import run_javascript


async def fetch(path: str):
    javascript_code = f"""
        const req = await fetch('{path}');
        const res = await req.text();
        return res
    """

    data = await run_javascript(
        code=javascript_code,
        timeout=5,
    )

    return data or None
