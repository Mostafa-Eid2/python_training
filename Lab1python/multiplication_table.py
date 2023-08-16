num = int(input("Enter a number: "))

table = []
for i in range(1, num + 1):
    row = []
    for j in range(1, i + 1):
        product = i * j
        row.append(product)
    table.append(row)

print(table)