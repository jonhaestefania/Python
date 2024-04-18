"""
The function input() is useful to enter information generally 
stores on a variable.
"""
print("\nFunction input takes an argument.")
indentification = input("What is your name?: ")
print(indentification)

user = input("\nPlease enter a valid username: ")
print(f"Welcome {user.title()}!!!")

# Writing a large prompt 
prompt = "\nWe can build user for the logistics systems."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"The user {name.title()} is accessing to the system...")

print("\nNumerical inputs")
age = input("How old are you? ")
print(age)

# Explicitely we can convert entered string data into numerical
# values using the int() function:

age = input("\nHow old are you? ")
age = int(age)

if age >= 18:
    print("You're an adult.")
else:
    print("You are too young even to vote!")

