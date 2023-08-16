print("this program is used to generate an array with a specific length generate an array")
print("of a specific length filled with integer numbers increased by one from start.")

def gen_arr(length, start):
    generated_array = []
    element = start
    for i in range(length):
        generated_array.append(element)
        element += 1
    return generated_array

while True:
    try:
        length = int(input("Enter the length of the array: "))
        start = int(input("Enter the starting number in the array: "))
        gened_arr = gen_arr(length, start)
        print("Generated array:", gened_arr)
        break  # Exit the loop on successful input
    except ValueError:
        print("Invalid input. Please enter valid number.")
