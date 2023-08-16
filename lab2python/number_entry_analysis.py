print("Welcome to Number Analysis!")
print("Enter numbers or 'done' to finish.")
print("Get total, count, and average.")
print("-------------------------------------------")

total = 0
count = 0

while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if user_input.lower() == 'done':
        break  # Exit the loop if the user enters 'done'

    try:
        number = float(user_input)  # Convert user input to a number
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers were entered.")
