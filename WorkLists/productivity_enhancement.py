"""
Writing productivity.py code more conciscely
"""

quantity = 1000
productivity = []

print(f"Start productivity: {quantity}")

for year in range(1, 6):
    quantity *= 2
    productivity.append(quantity)

print(f"Increase productivity L5Y: {productivity}")
