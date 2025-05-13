def subtract_seven(num):
    num = num - 7
    return num

def main():
    num = int(input("Enter a number: "))
    num = subtract_seven(num)
    print("The answer is", num)

if __name__ == "__main__":
    main()