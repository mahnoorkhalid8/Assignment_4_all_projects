def main():
    year = int(input("Enter a year here: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year!")

            else: 
                print("This is not a leap year!")
        else: 
            print("This is a leap year!")
    else: 
        print("This is not a leap year!")

if __name__ == "__main__":
    main()
