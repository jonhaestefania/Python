"""
For the last five years the total productivity by the trucks
has been duplicated in k deliveries yearly
"""
quantity = 1000
productivity = []

for year in range(1, 6):
    quantity = quantity * 2
    productivity.append(quantity)

print(productivity)
