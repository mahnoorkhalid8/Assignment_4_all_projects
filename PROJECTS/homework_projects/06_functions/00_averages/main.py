# first method

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = (num1 + num2) / 2

    print(total)

if __name__ == "__main__":
    main()


# second method

def average(a: float, b: float):
    sum = a + b
    return sum / 2

def main():
    avg1 = average(0, 10)
    avg2 = average(8, 10)
    
    final_avg = average(avg1, avg2)
    print("average 1:", avg1)
    print("average 2:", avg2)
    print("final average:", final_avg)

if __name__ == "__main__":
    main()