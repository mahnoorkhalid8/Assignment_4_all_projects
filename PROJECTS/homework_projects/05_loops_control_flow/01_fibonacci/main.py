MAXIMUM_NUMBER : int = 10000

def main():
    current_number = 0
    next_number = 1

    while current_number <= MAXIMUM_NUMBER:
        print(current_number)
        new_number = current_number + next_number
        current_number = next_number
        next_number = new_number

if __name__ == "__main__":
    main()