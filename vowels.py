def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in string:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count

input_string = input("Enter a string: ")
result = count_vowels(input_string)
print(f"Number of vowels in the string: {result}")

