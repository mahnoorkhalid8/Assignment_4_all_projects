import random

def main():
        num: int = random.randint(1, 99)
        print("I'm thing of a number in between 1-100")

        guess = int(input("Enter a number: "))

        while guess != num:
            if guess < num:
                print("Your guess is too small")
            else: 
                print("Your guess is too large")

            guess = int(input("Enter a new guess: "))
        print(f"Congrats! You guessed it right!\nThe number was {num}")

if __name__ == "__main__":
    main()