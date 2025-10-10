"""List Exercises"""

AMOUNT_OF_NUMBERS = 5


def main():
    numbers = get_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = calculate_average(numbers)
    print(f"The average of the numbers is {average}")


def get_numbers():
    numbers = []
    for i in range(AMOUNT_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


main()
