print("this program is used to print the locations of 'i' character in any added string")
string_added = input("please input a string: ")

n_characters = []
for index, char in enumerate(string_added):
    if char == "i":
        n_characters.append(index)
        
print(f"The character 'i' is found at indices: {n_characters}")