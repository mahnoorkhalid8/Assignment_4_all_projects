def main():
    num1: int = int(input("Enter an integer to be divided: "))
    num2: int = int(input("Enter an integer to divide by: "))
    remainder: int = num1 % num2                                 # Get the remaider
    quotient: int = num1 // num2                                 # Get the quotient (no remainder)
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}") 

if __name__ == "__main__":
    main()
