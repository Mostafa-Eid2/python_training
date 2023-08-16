print("..........................................................................")
print("A program to ensure the user entered his name nothing else")
print("..........................................................................")
#فضلت شوية ازود مجموعة خواص اضافية وربما اضافة المزيد لاحقا
def entername():
    while True:
        name = input("Please, enter your name, nothing else: ")
        if name.lower() == "exit":
            print("Exiting the program.")
            raise SystemExit  # Raise an exception to terminate the program
        elif name.isalpha():
            print("Valid Name; stored successfully")
            return name

name = entername()

def validate_email(email):
    while True:
        email = input("Please, enter your email address: ")
        if email.lower() == "exit":
            print("Exiting the program.")
            raise SystemExit  # Raise an exception to terminate the program
        if "@" in email and "." in email:
            at_index = email.index("@")
            dot_index = email.index(".")
            if at_index < dot_index:
                print("Valid Email; stored successfully")
                return email
            else:
                print("Invalid Email; please enter a valid email address")
        else:
            print("Invalid Email; please enter a valid email address")

email = input("Please, enter your email address: ")
if email.lower() == "exit":
    print("Exiting the program.")
    raise SystemExit  # Raise an exception to terminate the program
else:
    email = validate_email(email)

print("Name:", name)
print("Email:", email)
