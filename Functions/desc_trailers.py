def trailer(van_type, carrier, size, capacity):
    """ Display trailer information for all fleet. """
    print(f"\nThe trailer type is: {van_type.title()}.")
    if len(carrier) == 3:
        print(f"The service for this trailer is assigned to: {carrier.upper()}")
    else:
        print(f"The service for this trailer is assigned to: {carrier.title()}.")
    print(f"This trailer sizes: {size}Fts.")
    print(f"Total load capacity for this trailer is: {capacity}Tons.")

trailer('dry', 'tumsa', '48', '20')
trailer('livestock', 'accel', '40', '18')
trailer('reefer', 'transmex', '28', '14')
trailer('tanker', 'ala', '53', '20')

# Associating data trailers directly on a function
trailer(van_type='dry', carrier='tum', size=53, capacity=30)

# Setting default values
def type_of_service(carrier_name, type='dedicated'):
    """ Show the type of service for selected carrier. """
    if len(carrier_name) < 4:
        print(f"\nThe carrier: {carrier_name.upper()} provides {type} service.")
    else:
        print(f"\n{carrier_name.title()} is {type.title()} fleet.")

type_of_service(carrier_name='ala')
type_of_service('bucaneros', 'external')
type_of_service(carrier_name='walmart', type='private')
