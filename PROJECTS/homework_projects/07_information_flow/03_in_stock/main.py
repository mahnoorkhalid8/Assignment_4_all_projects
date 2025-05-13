def num_in_stock(fruit):
    if fruit == "apple":
        return 5
    if fruit == "banana":
        return 20
    if fruit == "mango":
        return 100
    else:
        return 0
    
def main():
    fruit: str = input("Enter fruit name: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock!")
    else:
        print("This ruit is in stock! Here is how many: ")
        print(stock)

if __name__ == "__main__":
    main()