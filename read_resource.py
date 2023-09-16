def read_props():
    from jproperties import Properties
    configs = Properties()
    with open('resources.properties', 'rb') as read_prop:
        configs.load(read_prop)
    prop_view = configs.items()
    result = {}
    for item in prop_view:
        result.__setitem__(item[0],item[1].data)
    return result
