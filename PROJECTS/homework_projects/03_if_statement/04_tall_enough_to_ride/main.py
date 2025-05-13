MIN_HEIGHT : int = 4            # height in feet

def main():
    print("Height should be in feet!!!")
    height = float(input("How tall are you? "))

    if height > MIN_HEIGHT:
        print("You're tall enough to ride!")
    elif height == MIN_HEIGHT:
        print("You can ride!")
    else:
        print("You're not tall enough to ride but may be next year:)")

if __name__ == "__main__":
    main()