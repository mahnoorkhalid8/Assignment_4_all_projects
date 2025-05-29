def phone_number():
    phonebook = {}

    while True:
        user_name = input("Name: ")
        if user_name == "":
            break
        user_number = input("Number: ")
        phonebook[user_name] = user_number

    return phonebook

def print_phone(phonebook):
    """Print all the names and numbers in the phonebook"""
    for user_name in phonebook:
        print(str(user_name) + "->" + str(phonebook[user_name]))

def lookup_nums(phonebook):
    """Lookingup the phone number in the phonebook"""

    while True:
        user_name = input("Enter name to lookup: ")
        if user_name == "":
            break
        if user_name not in phonebook:
            print(f"{user_name} is not in the phonebook!")
        else:
            print(phonebook[user_name])

def main():
    phonebook = phone_number()
    print_phone(phonebook)
    lookup_nums(phonebook)

if __name__ == "__main__":
    main()