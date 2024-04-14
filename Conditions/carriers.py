# Generally when you write a database for stores the names
# for all of those transportation carries you do in lower case
# or their names are presented in short abbreviature.
# The following code loops through a list of carrier names and 
# converts each name to propper or UPPER case when applies.

carriers = ['ala', 'narcea', 'tms', 'bucaneros', 'tumsa']

for carr in carriers:
    if len(carr) <= 3:
        print(carr.upper())
    else:
        print(carr.title())

# to find out whether a particular carrier in our list you can
# use the keyword in and assign to a variable for readability:

specialized = 'bucaneros'
if specialized in carriers:
    print("Yes, the carrier is authorized.")
else: 
    print("Carrier {specialized.title()} is not authorized for this load.")

