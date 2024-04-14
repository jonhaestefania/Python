# You might often face to data stores in lower or upper format
# and may be you need to combine in a single long string

first_name = 'jonha'
last_name = 'estefania'
full_name = f"{first_name} {last_name}"
print(full_name)

# The f-strings are useful to insert variable's value into a 
# single long string

long = f"{first_name} {last_name}"
print(f"The executive officer {long.title()}!")

# assign a full message to a variable and performs ormat with 
# two methods earlier mentioned.

message = f"{long.title()} is a Python Developer now."
print(message)

