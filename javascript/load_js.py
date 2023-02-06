from nicegui.ui import run_javascript


async def load_js(code: str, respond: bool = False):
    javascript_source = """
        function __python__load_js() {
            const script = document.createElement('script');

            script.textContent = script_code;

            console.log(`Aplicando Javascript na Aplicação!`);

            document.querySelector("#app").appendChild(script);
        }

        __python__load_js()
    """

    await run_javascript(
        code=f"const script_code = `{code}`; {javascript_source}",
        respond=respond,
    )
