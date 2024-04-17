# Dictionaries could be are a piece of database system and
# stores tons of key-value pairs.

manager = {
    'user': 'jestefania',
    'first_name': 'jonha',
    'last_name': 'estefania',
    'age': 42,
    'department': 'it',
}

for key, value in manager.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

managers = {
    'ana': 'finances',
    'rox': 'analytitcs',
    'nina': 'design',
    'jon': 'it',
}

for manager, department in managers.items():
    print(f"\n{manager.title()} is responsible for {department.title()} area.")

# Looping through list to compare values with keys in a dictionary
associates = ['jon', 'sam', 'ana', 'tybyry', 'rox', 'pedro', 'panchito', 'timon', 'gordito']
for associate in associates:
    print(associate.title())
  
    if associate in managers.keys():
        manager = managers[associate].title()
        print(f"\t{associate.title()} is a manager!")

# Looking for particular value 
managers = {
    'ana': 'finances',
    'rox': 'analytitcs',
    'nina': 'design',
    'jon': 'it',
}

if 'sam' not in managers.keys():
    print("\nSam is not a manager, he is the Chairman!")

# Sorting keys for accessing in particular order using the
# sorted() function:
associates = {
    'jon': 'it',
    'tybyry': 'yard',
    'rox': 'analytitcs',
    'nina': 'design',
    'ana': 'finances',
    'claudia': 'qa',
    'pedro': 'yard',
    'blanca': 'pallets',
    'naye': 'traffic',
    'alma': 'loss prevention',
}

print(f"\nRaw data: ")
print(associates)

print("\nShow the associates ascending order: ")
for associate in sorted(associates.keys()):
    print(f"{associate.title()} is on DC Mexico.")


# Similarly you can use the values() method to return a list of
# associates' department on the DC:
print("\nThese departments are covered for the next Peak session: ")
for department in associates.values():
    print(department.title())

# to see departments without repetition you can convert the 
# dictionary into a set using the set() function:
print("\nThese departments are covered without repetition: ")
for department in set(associates.values()):
    print(department.title())


