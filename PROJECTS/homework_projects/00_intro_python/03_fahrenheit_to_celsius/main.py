def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) *5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) +32

def main():
    print("🌡 Temperature Converter")
    print("1. Convert from Fahrenheit to Celsius")
    print("2. Convert from Celsius to Fahrenheit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        fahrenheit =float(input("Enter temperature in Fahrenheit:"))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")

    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius:"))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    else:
        print("❌Invalid choice! Please enter 1 or 2")

if __name__ == "__main__":
    main()