AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")
    user_input = input("").strip().lower()

    while user_input.lower() != AFFIRMATION.lower():
        print("That was not the affirmation")

        print(f"Please type the following affirmation: {AFFIRMATION}")
        user_input = input("").strip().lower()

    print("That's right!")

if __name__ == "__main__":
    main()
 
 