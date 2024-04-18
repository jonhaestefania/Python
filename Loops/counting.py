"""
The while loop allows to count up through a series of numbers.

"""

current_number = 1
while current_number <=10:
    print(current_number)
    current_number += 1

# We can make an script to answering to the user for the 
# inbound dock doors, we will define the quit condition 
# until the user enter the 'quit' word.
prompt = "\nPlease enter the door for the inbound dock to use."
prompt += "\nEnter 'quit' to end the program: "

door = ""
while door != 'quit':
    door = input(prompt)
    print(door)

# fix the above program to don't prints the word quit at 
# last value entering.
prompt = "\nPlease enter the door for the inbound dock to use."
prompt += "\nEnter 'quit' to end the program: "

door = ""
while door != 'quit':
    door = input(prompt)

    if door != 'quit':
        print(door)