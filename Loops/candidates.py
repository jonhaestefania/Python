candidates = {}

# Activate the flag for the candidates
recruiting = True

while recruiting:
    # Get the person's name and experience
    name = input("\nWhat is your name? ")
    experience = input("How many years of experience are you in logistics? ")

    # Store the data
    candidates[name] = experience

    # Check if more candidates are available
    interview = input("There are more candidates to interviewing? (yes/no) ")
    if interview == 'no':
        recruiting = False

# Recruiting is complete. Show the data.
print("\nDatabase...")
for name, experience in candidates.items():
    print(f"{name.title()} have {experience} years of experience in logistics.") 