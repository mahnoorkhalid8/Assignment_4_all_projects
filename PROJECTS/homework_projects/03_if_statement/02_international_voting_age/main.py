PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    print("What is your age?")
    user_age = int(input("Enter your age here: "))

    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You can not vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + "!")
    
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You can not vote in Stanlau where the voting age is " + str(STANLAU_AGE) + "!")
    
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You can not vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + "!")

if __name__ == "__main__":
    main()




