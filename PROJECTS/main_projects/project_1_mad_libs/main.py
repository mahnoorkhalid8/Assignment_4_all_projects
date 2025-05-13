def main():
    noun1: str = input("Enter the first noun: ")
    noun2: str = input("Enter the second noun: ")
    noun3: str = input("Enter the third noun: ")
    adj1: str = input("Enter the first adjective: ")
    adj2: str = input("Enter the second adjective: ")
    adj3: str = input("Enter the third adjective: ")
    place_name: str = input("Enter a place name: ")

    story = (
        f"""Once upon a time in {place_name}, there was a {adj1} {noun1} who dreamed of adventure. 
        One day, while exploring the outskirts of {place_name}, the {noun1} stumbled upon a {adj2} {noun2}. 
        Intrigued, they decided to approach the {noun2}, only to discover it was guarding a {adj3} {noun3}. 
        Realizing this was the opportunity they had been waiting for, the {noun1} befriended the {noun2}, 
        and together, they embarked on a journey that would change their lives forever."""
    )

    print("Here is your story:)")
    print(story)

if __name__ == "__main__":
    main()