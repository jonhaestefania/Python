# In this program we can use the break statement to stop
# running the program and exit for a while loop.
prompt = "\nPlease enter the DC name for send the shipments: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    dc = input(prompt)

    if dc == 'quit':
        break
    else:
        print(f"We sent the shipments to: {dc.title()}")
