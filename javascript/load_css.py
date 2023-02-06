from nicegui.ui import run_javascript


async def load_css(code: str):
    javascript_source = """
        function __python__load_css() {
            const style = document.createElement('style');

            style.setAttribute('type', 'text/css');
            style.textContent = css_code;

            console.log(`Aplicando CSS na Aplicação!`);

            document.querySelector("#app").appendChild(style);
        }

        __python__load_css()
    """

    await run_javascript(
        code=f"const css_code = `{code}`; {javascript_source}",
        respond=False,
    )
