# The following code shows how to build a list of dictionaries
truck1 = {'carrier': 'tms', 'area': 'inbound', 'yard_slot': 'F'}
truck2 = {'carrier': 'bucaneros', 'area': 'inbound', 'yard_slot': 'H'}
truck3 = {'carrier': 'tumsa', 'area': 'outbound', 'yard_slot': 'I'}

fleet = [truck1, truck2, truck3]

print()
for truck in fleet:
    print(truck)

# Making a large list for our dedicated fleet
tms = []

for truck_number in range(100):
    new_truck = {'carrier': 'tms', 'area': 'inbound', 'kilometers': 0}
    tms.append(new_truck)

# Get a set for 10 trucks:
print()
for truck in tms[:10]:
   print(truck)
print("...")

# Count the total quantity for the whole fleet
print(f"All available fleet: {len(tms)}")

# Assign 25 trucks to Tumsa dedicated fleet and outbound area
print("\nThe fleet are changed: ")
for truck in tms[24:49]:
    if truck['carrier'] == 'tms':
        truck['carrier'] = 'Tumsa'
        truck['area'] = 'outbound'
        truck['kilometers'] = 100

# Show this changes
for truck in tms[20:30]:
   print(truck)

