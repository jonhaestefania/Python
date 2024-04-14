"""
The numbers in Python there are integers and floats, the operations
between integer and integer returns an integer, the operations
between floats and anybody number type always returns an float.
"""

# integers
print("Integers:")
print("Sum 2 + 2: ", 2+2)

# floats
print("\nFloats: ")
print("Sum 2.0 + 3.0: ", 2.0 + 3.0)

# mixed
print("\nMixed: ")
print("Sum 3 + 4.0: ", 3 + 4.0)

# To write too long numbers, you can group them using 
# inderscores for readibility
most_distant_galaxy = 35_000_000_000_000
print(f"\nThe most distant galaxy distance is: {most_distant_galaxy}")

# Multiple assignment is possible on Python
print("\nMultiple assigment: ")
a, b, c = 1, 2, 3
print("a values: ", a)
print("b values: ", b)
print("c values: ", c)

# Contants are write using capital letters
OPEN_PORTS = 1000
print(f"\nMy Linux open ports to hack me are: {OPEN_PORTS}")

