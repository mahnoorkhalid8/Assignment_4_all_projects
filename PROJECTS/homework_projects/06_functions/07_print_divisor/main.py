def print_divisor(num: int):
    for i in range(num):
        divisor = i + 1
        if num % divisor == 0:
            print(divisor)

def main():
    input_num = int(input("Enter number: "))
    print_divisor(input_num)

if __name__ == "__main__":
    main()