# first way
def add_many_numbers(numbers: list[int]) -> int:
    """Takes a list of numbers and return the sum of those numbers"""
    return sum(numbers)

def main():
    numbers: list[int] = [1, 2, 3, 4]
    sum_of_numbers = add_many_numbers(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()

    

# second way (using for loop)
def add_many_numbers(numbers: list[int]) -> int:
    """Takes a list of numbers and return the sum of those numbers"""

    total: int = 0
    for number in numbers:
        total += number

    return total

def main():
    numbers: list[int] = [1, 2, 3, 4]
    sum_of_numbers = add_many_numbers(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()