def print_multiple(message: str, repeat: int):
    for i in range(repeat):
        print(message)

def main():
    input_message = input("Enter your message: ")
    input_times = int(input("How many ties you wanna repeat your message? "))
    print_multiple(input_message, input_times)

if __name__ == "__main__":
    main()