from javascript.fetch import fetch


async def fetch_api(route: str):
    data = await fetch(f"/api/{route}")
    return data or str()
