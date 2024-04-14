"""
For the demostration of slices we  consider this DC managers 
list, and we specify the index of the list and the elements 
that want to work with.
"""

managers = ['jeff', 'steve', 'sam', 'satya', 'elon']
print(f"The managers are: {managers}")
print(f"This managers are of QA: {managers[2:5]}")

# Omitting first index tells to Python automatically starts 
# the slice at the beginning of the list
print(managers[:3])

# If the second index is omitted the slice includes all items
# from the start specific index to last item
print(managers[2:])

# Negative index returns elements from the end of list to the 
# position mentioned at the negative index, in this code we
# call to the last 2 managers
print(managers[-2:])

# Or if you prefer call to the first 2 managers write this code
print(managers[:3])

# Select a subset of the elements in managers list
print("\nHere are the 2024 top 3 managers: ")
for manager in managers[:3]:
    print(manager.title())

# Copy the managers list to another called old_managers
old_managers = managers[:]
print("\nThe old managers are: ")
print(old_managers)

# Adding new elements to both lists:

print("\nCurrent managers: ")
print(managers)
quit_manager = managers.pop()
old_managers.append(quit_manager)
add_manager = 'larry'
managers.append(add_manager)
print("Update managers lists: ")
print(managers)
print(old_managers)
