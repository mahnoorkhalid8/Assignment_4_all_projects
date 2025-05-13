def even(even_list):
    count = 0
    for number in even_list:
        if number % 2 == 0:
            count += 1
    print(count)

def get_even_list():
    even_list = []
    user_input = input("Enter an integer or press enter to stop: ")
    
    while user_input != "":
        even_list.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return even_list

def main():
    even_list = get_even_list()
    even(even_list)

if __name__ == "__main__":
    main()
