def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 1:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("You can only choose 0, 1 or 2. Can not ake sentence!\nSorry.")

def main():
    word: str = input("Please type a Noun, Verb or Adjective:")
    print("Is this a Noun, Verb or Adjective?")
    part_of_speech = int(input("Type 0 for Noun, 1 for Verb and 2 for Adjective..."))
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()