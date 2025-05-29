def main():
    fruits = {"apple": 20.5, "mango": 40, "kiwi": 66, "strawberry": 85.5, "banana": 62, "cherry": 97, "dragonfruit": 109}

    initial_cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        amount_bought = int(input(f"How many {fruit} you wanna buy?"))
        initial_cost += price * amount_bought

    print(f"Your total is ${initial_cost}")

if __name__ == "__main__":
    main()