# To check wether two conditions are both True simultaneosly
# use the keyword and.
# Do not forget use the == operator to compare values.

carrier = 'tumsa'
shipment = 123

if carrier == 'tumsa' and shipment == 123:
    print("This load can be assign a new deliver.")
else:
    print("Please verify shipment data to reduce risk!")


dedicated = 'tms'
local = 'tumsa'

if (dedicated == 'tms' and local == 'tumsa'):
   print("Both carriers are specialized fleet.")
else:
    print("Plese check the carriers for this load.")


