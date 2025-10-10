""""Quick Pick" Lottery Ticket Generator"""

import random

AMOUNT_OF_NUMBERS_FOR_EACH_PICK = 6
LOW = 1
HIGH = 10

# TODO: ascending order

def main():
    number_of_picks = get_valid_number_of_picks()
    for i in range(number_of_picks):
        pick_numbers = []
        for j in range(AMOUNT_OF_NUMBERS_FOR_EACH_PICK):
            number = get_new_random_number(pick_numbers)
            pick_numbers.append(number)
            print(f"{number:2}", end=' ')
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


main()
