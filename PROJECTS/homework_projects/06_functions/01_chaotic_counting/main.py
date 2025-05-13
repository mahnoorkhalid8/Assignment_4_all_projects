import random

DONE_LIKELIHOOD = 0.3  # 30% chance of stopping

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def chaotic_count():
    for i in range(10):
        current_number = i + 1
        if done():
            return
        print(current_number)

def main():
    print("I'm going to count until 10 or until I feel like stopping whichever comes first")
    chaotic_count()
    print("I'm done!")

if __name__ == "__main__":
    main()