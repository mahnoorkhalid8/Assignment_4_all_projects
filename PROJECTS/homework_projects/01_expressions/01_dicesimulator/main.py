import random

NUM_SIDES = 6

def roll_dice():
    """Roll two dices and return total"""
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    total: int = dice1 + dice2
    print(f"Total: {dice1} + {dice2} = {total}")

roll_dice()