PROMPT: str = "What do you want?"
JOKE: str = "Why did the bicycle fall over? Because it was two-tired."
SORRY: str = "Sorry I only tell jokes!"

def main():
    user_input = input("Enter here: ")
    user_input = user_input.strip().lower()

    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()