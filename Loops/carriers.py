# The following carriers will be pass from the external to
# dedicated fleet
external_fleet = ['ala', 'tum', 'extra', 'suid']
dedicated_fleet = []

# Move each carrier from external fleet into the dedicated fleet
# list
while external_fleet:
    current_carrier = external_fleet.pop()

    print(f"Passing carrier: {current_carrier}")
    dedicated_fleet.append(current_carrier)

# Show all carriers in the dedicated list
print("\nThis is the dedicated fleet available: ")
for dedicated in dedicated_fleet:
    if len(dedicated) <= 3:
        print(dedicated.upper())
    else:
        print(dedicated.title())
     