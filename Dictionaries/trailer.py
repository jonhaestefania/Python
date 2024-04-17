# A dictionary in Python is a collection of key-value pairs. 
# In this example we create a simple dictionary to store 
# information about our trailers on we own our fleet.

trailer = {"plate": "123abc", "size": 28, "color": "white", "temperature": "dry"}

# To get values associated with a key, we can pass the name of 
# the key inside square brackets [].

print(trailer["plate"])
print(trailer["temperature"])

feets = trailer["size"]
print(f"This trailer's lenght is {feets} feets.")

# to add a new key-value pair, you must give the name of 
# dictionary and the new value.

trailer["yard_slot"] = "A"
trailer["slot_position"] = 10
print(f"\nTrailer data: {trailer}")

# Another way that write a dictionary is using an empty dictionary

# In this empty set we can add key-value pairs using the same 
# notation.

trailer2 = {}
trailer2["plate"] = "123def"
trailer2["size"] = 53
trailer2["color"] = "white"
trailer2["temperature"] = "dry"
trailer2["yard_slot"] = "E"
trailer2["slot_position"] = 12
print(f"\nAnother trailer data: {trailer2}")

# Python allows modifying values in dictionary to do this, 
# we need give the name of the dictionary and pass the key in
# square brackets and then assign the new value for this key.

trailer2["color"] = "gray"
print(f"\nThe trailer color is change: {trailer2}")

# At DC is very common to move trailers from yard to inbound or
# outbound areas.

trailer3 = {'yard_slot': 'F', 'slot_position': 510}
source_position = f"{trailer3['yard_slot']}{trailer3['slot_position']}"

# Move the trailer to any place in the DC
move_to = 'outbound' # or 'outbound'
new_position = 101 # for inbound values from 1 to 100 otbound 101 to 200

if move_to == 'inbound':
    target_position = f"{move_to}{new_position}"
    print(f"\nThe trailer will be recived in {target_position}")
elif move_to == 'outbound':
    target_position = f"{move_to}{new_position}"
    print(f"\nThe trailer will be loaded in {target_position}")
else:
    print("\nTrailer moves no changes.")

print(f"Trailer source position was: {source_position} and it moves to: {target_position}")

# The 'del' statement is used to remove key-value pairs
print(f"\nActual data of my fleet: {trailer2}")
del trailer2['color']
print(f"Color is no longer needed: {trailer2}")
