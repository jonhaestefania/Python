# The it department details are stored in the following
# dictionary which includes list into dictionary key:

it = {
    'manager': 'jon',
    'associates': ['tybyry', 'gordito', 'chino', 'peluchin'],
    'extension': 1010,
    'technologies': ['python', 'c', 'sql', 'linux'],
}

# Querying
print("The IT department associates are: ")
for associate in it['associates']:
    print("\t" + associate.title())

print(f"And reports to: {it['manager'].title()}.")

print("This area works with the following technologies: ")
for tech in it['technologies']:
   print("\t" + tech)


