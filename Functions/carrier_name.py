# Shows the formatted name for the external carriers
def carrier_name(service_type, short_name):
    """ Return a full name formatted. """
    full_carrier = f"{service_type} {short_name}"
    return full_carrier.title()

c1 = carrier_name('external', 'ala')
print(c1)
c2 = carrier_name('external', 'tms')
print(c2)
c3 = carrier_name('external', 'tum')
print(c3)

