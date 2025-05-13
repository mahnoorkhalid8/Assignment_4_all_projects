SENTENCE_START :str = "Hey! This is the mad lib for you, that provides the information that is passed by you...."

def main():
    adjective: str = input("Please type an adjective and press enter!")
    noun: str = input("Please type a noun and press enter!")
    verb: str = input("Please type a verb and press enter!")

    print(f"{SENTENCE_START} {adjective} {noun} {verb}")

if __name__ == "__main__":
    main()