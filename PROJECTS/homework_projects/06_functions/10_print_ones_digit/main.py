def print_ones(number):
    print("The ones digit is =", number % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones(num)

if __name__ == "__main__":
    main()