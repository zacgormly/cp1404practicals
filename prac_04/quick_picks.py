""""Quick Pick" Lottery Ticket Generator"""

import random

AMOUNT_OF_NUMBERS_PER_PICK = 6
LOW = 1
HIGH = 45


def main():
    """Program to generate an amount of picks based on user input."""
    number_of_picks = get_valid_number_of_picks()
    for i in range(number_of_picks):
        pick_numbers = []
        for j in range(AMOUNT_OF_NUMBERS_PER_PICK):
            number = get_new_random_number(pick_numbers)
            pick_numbers.append(number)
        pick_numbers.sort()
        print_formatted_pick(pick_numbers)


def get_new_random_number(pick_numbers):
    """Get a random number between LOW and HIGH not already in its pick."""
    number = random.randint(LOW, HIGH)
    while number in pick_numbers:
        number = random.randint(LOW, HIGH)
    return number


def get_valid_number_of_picks():
    """Get a valid positive integer number of picks."""
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid number of picks.")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


def print_formatted_pick(pick_numbers):
    """Print pick numbers with neat format."""
    print(" ".join(f"{number:2}" for number in pick_numbers))


main()
