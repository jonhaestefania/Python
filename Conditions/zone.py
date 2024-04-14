# You can use the keyword 'not' if you know if a value does 
# not appear in a list.

external_fleet = ['castores', 'suvi', 'bosco', 'tum']
carrier = 'tms'

if carrier not in external_fleet:
    print(f"Carrier {carrier.title()} is private fleet.")
else:
    ("This carrier is external.")

zones = [1, 2, 3, 4, 5, 6, 7]
zone = 8

if zone not in zones:
    print(f"The zone {zone} has not been defined yet.")

# Boolean values are valid, this expressions can be write
# as only true or false values.

# truck_available = true
# ready_to_load = true
# on_time = false

# choose an appropiate carrier for the distance
distance = 1200

if distance < 100:
    print("Carrier TMS is recommended.")
elif distance < 500:
    print("Carrier Tumsa is recommended.")
else:
    print("Carriers Suvi or Castores are recommended.")
