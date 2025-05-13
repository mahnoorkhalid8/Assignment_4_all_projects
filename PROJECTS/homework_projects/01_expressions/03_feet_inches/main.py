def inches_to_feet(inches):
    return inches // 12

def feet_to_inches(feet):
    return feet * 12

def main():
    """Feet and Inches Converter"""
    print("1. Convert from Inches to Feet")
    print("2. Convert from Feet to Inches")

    choose = int(input("Enter your choise: "))

    if choose == 1:
        Inches = float(input("Enter length in inches: "))
        Feet = inches_to_feet(Inches)
        print(f"{Inches} inches = {Feet} feet")

    elif choose == 2:
        Feet = float(input("Enter length in feet: "))
        Inches = feet_to_inches(Feet)
        print(f"{Feet} feet = {Inches} inches")

    else:
        print("❌Invalid choice! Please enter 1 or 2")

if __name__ == "__main__":
    main()