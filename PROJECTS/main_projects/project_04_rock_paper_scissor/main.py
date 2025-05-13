import random

def main():
    print("Welcome to Rock, Paper, Scissor Game!")
    user_input = input("What's your choice?'r' for rock, 'p' for paper and 's' for scissor").lower()
    computer_input = random.choice(["r", "p", "s"])
    user_score = computer_score = 0

    if user_input == computer_input:
        print("It's a tie")
        user_score = computer_score
    
    elif is_win(user_input, computer_input):
        print("You won:)")
        user_score += 1
        
    else:
        print("You lost:(")
        computer_score += 1

    print(f"Current score:\n Your score: {user_score}\n computer score: {computer_score}")

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    return False
    
if __name__ == "__main__":
    main()