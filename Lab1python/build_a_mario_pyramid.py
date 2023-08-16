# Step 1: User Input
num = int(input("Enter a number: "))

# Step 2: Build Mario Pyramid
for i in range(1, num + 1):
    spaces = ' ' * (num - i)
    stars = '*' * i
    print(spaces + stars)
