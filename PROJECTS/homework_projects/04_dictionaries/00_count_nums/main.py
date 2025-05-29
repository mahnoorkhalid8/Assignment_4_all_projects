def get_user_number():
    user_num = []

    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break

        num = int(user_input)
        user_num.append(num)

    return(user_num)

def user_nums_count(number_list):
    new_dict = {}
    for num in number_list:
        if num not in new_dict:
            new_dict[num] = 1

        else:
            new_dict[num] += 1

    return new_dict

def print_num_counts(new_dict):
    for num in new_dict: 
        print(f"{num} appears {new_dict[num]} times.")

def main():
    user_num = get_user_number()
    new_dict = user_nums_count(user_num)
    print_num_counts(new_dict)

if __name__ == "__main__":
    main()

