def update_data_from_api(api_element, table_instance):
    data = api_element.get_all()
    table_instance.options["rowData"] = [item.to_dict() for item in data]
    table_instance.update()


def default_col_def():
    return {
        "sortable": True,
        "filter": True,
        "floatingFilter": True,
    }
