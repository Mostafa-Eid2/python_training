print("This program is used to count the number that the word 'iti was mentioned in a text")
input_string = input("Please enter a string: ")

count = 0

words = input_string.split()

for word in words:
    if word.lower() == 'iti':
        count += 1
        
print(count)