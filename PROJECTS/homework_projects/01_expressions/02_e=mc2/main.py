C : int = 299792458

def energy():
    m = float(input("Enter mass in kg: "))
    e = m* (C**2)

    print("e = m* C^2")
    print("m = " + str(m) + "kg")
    print("C = " + str(C) + "m/s")

    print(f"Enery = {e} joules of energy.")

energy() 