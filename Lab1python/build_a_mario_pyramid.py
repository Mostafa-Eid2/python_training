num = int(input("Enter a number: "))

for i in range(1, num + 1):
    spaces = ' ' * (num - i)
    stars = '*' * i
    print(spaces + stars)