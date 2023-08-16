user_array = []

for i in range(5):
    user_input = int(input(f"Enter element {i + 1}: "))
    user_array.append(user_input)

ascending_sorted_array = sorted(user_array)
descending_sorted_array = sorted(user_array, reverse=True)

print("Original array:", user_array)
print("Ascending sorted array:", ascending_sorted_array)
print("Descending sorted array:", descending_sorted_array)
print("note that the original array didn'y change : signature :Mostafa : i am mostafa not AI :D")
print("I know that i could use list.sort() if i wanted it to be permenently modifed or even store the new output in the variable ")