import random

NUM_ROUND = 5

def main():
    print("WELCOME TO HIGH-LOW GAME:)")
    initial_score = 0

    for i in range(NUM_ROUND):
        print("Round", i + 1)

        computer_number : int = random.randint(1, 100)
        user_number : int = random.randint(1, 100)
        print("Your number is", user_number)

        guess : str = input("Do you think your number is higher or lower than the computer's?: ")

        while guess != "higher" and guess != "lower":
            guess = input("Please enter either higher or lower: ")

        high : bool = guess == "higher" and user_number > computer_number
        low: bool = guess == "lower" and user_number < computer_number

        if high or low:
            print("You were right!\nThe computer's guess was", computer_number)
            initial_score += 1
        else:
            print("You were wrong:(\nThe computer's guess was", computer_number)

        print("Your score is now", initial_score)
        print()
    
    print("Your final score is", initial_score)

    if initial_score == NUM_ROUND:
        print("WOW!!! You played perfectly:)")

    elif initial_score > NUM_ROUND // 2:
        print("Good Job! You played really well!!")

    else:
        print("Better luck next time:(")

if __name__ == "__main__":
    main()