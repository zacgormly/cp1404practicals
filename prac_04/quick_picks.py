""""Quick Pick" Lottery Ticket Generator"""

import random

AMOUNT_OF_NUMBERS_FOR_EACH_PICK = 6
LOW = 1
HIGH = 45


def main():
    number_of_picks = get_valid_number_of_picks()
    for i in range(number_of_picks):
        pick_numbers = []
        for j in range(AMOUNT_OF_NUMBERS_FOR_EACH_PICK):
            number = get_new_random_number(pick_numbers)
            pick_numbers.append(number)
        ascending_numbers = order_pick_numbers(pick_numbers)
        print_formatted_pick(ascending_numbers)
        print()


def get_new_random_number(pick_numbers):
    number = random.randint(LOW, HIGH)
    while number in pick_numbers:
        number = random.randint(LOW, HIGH)
    return number


def get_valid_number_of_picks():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Invalid number of picks.")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


def print_formatted_pick(ascending_numbers):
    for number in ascending_numbers:
        print(f"{number:2}", end=' ')


def order_pick_numbers(pick_numbers):
    ascending_numbers = [number for number in sorted(pick_numbers)]
    return ascending_numbers


main()
