MAX_LENGTH = 3

def shorten(my_list):
    while len(my_list) > MAX_LENGTH:
        last_element = my_list.pop()
        print(last_element)

def get_list():
    """Prompts the user to enter one element of the list at a time and returns the resulting list"""

    new_list = []
    user_input: str = input("Enter an element of the list or press enter to stop. ")
    while user_input != "":
        new_list.append(user_input)
        user_input = input("Enter an element of the list or press enter to stop. ")
    return new_list

def main():
    new_list = get_list()
    shorten(new_list)

if __name__ == "__main__":
    main()
