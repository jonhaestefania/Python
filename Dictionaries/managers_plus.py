# Of course a dictionary can nest a dictionary inside, this
# data structure is look a JSON document:

managers = {
    'jestefania': {
        'first_name': 'jon',
        'last_name': 'estefania',
        'age': 42,
        'location': 'DC 1 Mexico',
        },
    'aramirez': {
        'first_name': 'ana',
        'last_name': 'ramirez',
        'age': 37,
        'location': 'DC 2 Jalisco',
        }
}

for manager, manager_info in managers.items():
    print(f"\nManager: {manager}")
    full_name = f"{manager_info['first_name']} {manager_info['last_name']}"
    location = manager_info['location']

    print(f"\tFull name_ {full_name.title()}")
    print(f"\tLocation: {location.title()}")

