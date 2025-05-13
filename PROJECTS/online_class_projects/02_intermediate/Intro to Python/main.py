MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    earth_weight_input = float(input("Enter your weight: "))
    planet_input = input("Enter a planet: ")

    if planet_input == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet_input == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet_input == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet_input == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet_input == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet_input == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else: 
        gravity_constant = NEPTUNE_GRAVITY
    

    planetary_weight = earth_weight_input * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    print(f"The equivalent weight on {planet_input} = {rounded_planetary_weight}")

if __name__ == "__main__":
    main()