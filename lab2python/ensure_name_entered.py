print("..........................................................................")
print("A program to ensure the user entered his name nothing else")
print("..........................................")
while True
def entername():
    name = input("Please, enter your name, nothing else: ")
    if name.isalpha():
        print("Valid Named; stored successfully")
    else:
        print("Inalid Named; please enter only letters...")
entername()