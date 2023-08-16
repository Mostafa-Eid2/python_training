print("..........................................................................")
print("A program to ensure the user entered his name nothing else")
print("..........................................")
def entername():
        name = input("Please, enter your name, nothing else: ")
        if name.isalpha():
            print("Valid Named; stored successfully")
        else:
            print("Inalid Named; please enter only letters...")
entername()

def validate_email(email):
    if "@" in email and "." in email:
        at_index = email.index("@")
        dot_index = email.index(".")
        if at_index < dot_index:
            print("Valid Email; stored successfully")
        else:
            print("Invalid Email; please enter a valid email address")
    else:
        print("Invalid Email; please enter a valid email address")

while True:
    email = input("Please, enter your email address: ")
    validate_email(email)
