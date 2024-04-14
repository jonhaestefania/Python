"""
To create a list in Python we write the elements in the list
separated by commas and we use square brackets ([]) to surrounded
this list. 
"""
print("List of carriers:")
carriers = ['castores', 'tum', 'bosco', 'tms', 'specialized', 'ala']
print(carriers)

# to access an element in a list write the name of the list
# follow by the index 
print("\nThe third carrier:")
print(carriers[2])

# We can use string methods to formatting the element in the list
print("\nFormatting strings:")
print(carriers[2].title())

# In Python all items in the list starts at 0 position
print("\nThe first item: ")
print(carriers[0].title())

# On the other hand, Python always return the last item asking
# for the item at index -1.
print("\nThe last item: ")
print(carriers[-1].title())

#  Using f-strings we can accessing to individual values from a list
print("Using individual values")
message = f"Carrier {carriers[2].title()} is assigned to local deliveries."
print(message)

# To change an element, use the name of the list followed by the
# index of the element you want to change and then provide the 
# new value you want that item you have

# Modifying elements in a list
print("\nModifying the first element")
carriers[0] = 'narcea'
print(carriers)

# The append() method allows to add a new element to our list
print("\nAppending elements")
carriers.append('tumsa')
print(carriers)

# If we start with an empty list and then we can add items
# using append() method.
print("\nBuild dynamically lists")
states = []

states.append('yucatan')
states.append('mexico')
states.append('cdmx')
states.append('sinaloa')
states.append('michoacan')

print(states)

# The method insert() allows to insert a new element at any
# position, you do this specifying the index of the new element
# and the value
print("\nInserting elements")
states.insert(3, 'morelos')
states.insert(0, 'veracruz')
print(states)

# To remove elements from a list you use the del statement
# as follows
print("\nRemoving elements from a list")
del states[3]
print(states)

# The pop() method removes the last item in a list
print("\nRemove last item using pop()")
popped_state = states.pop()
print(states)
print(popped_state)

# The pop method also allows to remove an item from any position
# in the list, do this including the index of the item that want
# to remove
print("\nRemoving by position using pop()")
state_cover = states.pop(2)
print(f"This carrier covers routes to: {state_cover.title()}")

# Another form to remove elements from a list is by value
# using the remove() method
print("\nRemove items by value")
print(states)
to_far = 'sinaloa'
states.remove(to_far)
print(states)
print(f"To far: {to_far.title()}")

# The sort() method is used to sort a list
print("\nSorting lists")
print("Unordered list:")
print(carriers)
print("\nSorted list")
carriers.sort()
print(carriers)
carriers.sort(reverse=True)
print("\nSort list in alphabetical reverse order:")
print(carriers)

# The sorted() function is used to maintain the original order
print("\nOriginal order:")
print(carriers)
print("Sorted list without affecting the original order: ")
print(sorted(carriers))

# We can use the reverse() method to reverse the original order
# of a list
print("\nReverse order of a list")
print(carriers)
carriers.reverse()
print(carriers)

# The len() function is used allows to find the length of 
# a list
print("\nFinding the length of carriers list:")
print(len(carriers))

 
