function __python__add_css() {
    const style = document.createElement('link');

    style.setAttribute('rel', 'stylesheet');
    style.setAttribute('type', 'text/css');
    style.setAttribute('href', `/static/css/${css_file_name}.css`);

    console.log(`Adding css file: ${css_file_name}`);

    document.querySelector("#app").appendChild(style);
}

__python__add_css()