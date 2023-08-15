print("This program is used to generate briefs for words with no vowels")
def remove_vowels(word):
    vowels = 'aeiouAEIOU'
    
    brief_word = ''
    for char in word:
        if char not in vowels:
            brief_word += char
            
    return brief_word

while True:
    input_word = input("Enter a single word: ")
    if ' ' not in input_word:
        break
    else:
        print("Please enter a single word without spaces.")

brief_version = remove_vowels(input_word)
print(f"The brief version of '{input_word}' is '{brief_version}'.")