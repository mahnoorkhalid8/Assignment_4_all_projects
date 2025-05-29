import random

DICE_SIDES : int = 6

def main():
    """Roll two dices and get the total"""

    dice1: int = random.randint(1, DICE_SIDES)
    dice2: int = random.randint(1, DICE_SIDES)
    total: int = dice1 + dice2

    print(f"Dice have {DICE_SIDES} sides")
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total of two dices: {total}")

if __name__ == "__main__":
    main()
