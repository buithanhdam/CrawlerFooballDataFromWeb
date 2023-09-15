def read_url_props():
    from jproperties import Properties
    configs = Properties()
    with open('resources.properties', 'rb') as read_prop:
        configs.load(read_prop)
    prop_view = configs.items()
    result = []
    for item in prop_view:
        if item[0] != 'CSV_PATH':
            result.append(item[1].data)
    return result


def read_csv_props():
    from jproperties import Properties
    configs = Properties()
    with open('resources.properties', 'rb') as read_prop:
        configs.load(read_prop)
    prop_view = configs.items()
    result = []
    for item in prop_view:
        if item[0] == 'CSV_PATH':
            result.append(item[1].data)
    return result
