ADULT_AGE : int = 18            #US age

def is_adult(age: int):
    if age >= ADULT_AGE:
        print("Entered age is an adult age.")
        return True
    
    print("Entered age is not an adult age.")
    return False

def main():
    age : str = int(input("How old is this person? "))
    print(is_adult(age))

if __name__ == "__main__":
    main()