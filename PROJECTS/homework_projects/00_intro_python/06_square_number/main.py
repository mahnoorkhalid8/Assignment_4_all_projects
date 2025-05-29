def square_number():
    number: float = float(input("Enter a number to get it's square: "))
    square: float = number ** 2

    print("The square of", number, "is", square)
    
square_number()