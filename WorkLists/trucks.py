"""
You can use the Python's range() function to create series
of numbers, for this example create a fleet of trucks.
"""

print("\nMy fleet: ")
for truck in range(0, 10):
    print(truck)

# The range above are presented is flat and is not stored on
# a list, fix it doin this
print("\nMy trucks list into a variable")
trucks = list(range(0, 10))
print(f"Trucks: {trucks}")



