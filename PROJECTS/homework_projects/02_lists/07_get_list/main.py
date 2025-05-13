def get_list():
    """Prompts the user to enter one element of the list at a time and returns the resulting list"""

    new_list = []
    user_input: str = input("Enter an element of the list or press enter to stop. ")
    while user_input != "":
        new_list.append(user_input)
        user_input = input("Enter an element of the list or press enter to stop. ")
    print("Here is the list:", new_list)

get_list()


