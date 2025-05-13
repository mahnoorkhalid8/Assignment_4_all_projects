def get_first_element(my_list):
    """Print first element of a provided list"""
    if my_list:
        print(my_list[0])
    else:
        print("List is empty, no first element to display!")

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
    get_first_element(new_list)

if __name__ == "__main__":
    main()

