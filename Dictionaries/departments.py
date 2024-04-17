# When you use a dictionary to store one kind of information
# you can write the dictionary structure follow this structure:

managers = {
    'claudia': 'statistics',
    'any': 'finances',
    'jon': 'it',
    'naye': 'traffic',
    'carolina': 'qa',
    'nina': 'design',
    'roxi': 'analytics',
}

department = managers['jon'].title()
print(f"Jon is responsible for {department} department.")

