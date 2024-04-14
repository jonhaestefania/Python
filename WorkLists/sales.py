"""
In this example we can find minimum, maximum, average and sum
of the last 10 years sales.
"""
print("Simple statistics")

sales = [1290, 1435, 2201, 2439, 2615, 2342, 2614, 2709, 2800, 2921]
print("\nSales in millions: ")
print(sales)

min = min(sales)
max = max(sales)
sum = sum(sales)
avg = (sum/len(sales))

print(f"\nMinimum: {min}\nMaximum: {max}\nSum: {sum}\nAverage: {avg}")
