import math

def theorem():
    AB: float = float(input("Enter the length of AB: "))
    AC: float = float(input("Enter the length of AC: "))

    BC: float = AB ** 2 + AC ** 2
    BC = math.sqrt(BC)

    print(f"The length of BC (the hypotenuse) is: {BC}")

theorem()

