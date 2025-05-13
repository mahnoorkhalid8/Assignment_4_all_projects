def access_element(my_list, index):
    try:
        return my_list[index]
    except:
        return "Index out of range!"
    
def modify_list_element(my_list, index, new_element):
    try:
        my_list[index] = new_element
        return my_list
    except:
        return "Index out of range!"
    
def slice_element(my_list, start, end):
    try:
        return my_list[start:end]
    except:
        return "Invalid indices."
    
def list_game():
    my_list = [1, 2, 3, 4, 5]
    print("Current list:", my_list)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter an operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(my_list, index))

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_element = input("Enter new element: ")
        print(modify_list_element(my_list, index, new_element))

    elif operation == "slice":
        start = int(input("Enter starting index: "))
        end = int(input("Enter ending index: "))
        slice_element(my_list, start, end)

    else:
        print("Invalid operation!!!")

list_game()
print()
print()
print()
print()
print()
print()

def main():
    fruit_list = ["apple", "banana", "kiwi", "strawberry"]
    list_len = len(fruit_list)
    print(list_len)

    fruit_list.append("mango")

    for fruit in fruit_list:
        print(fruit)

if __name__ == "__main__":
    main()