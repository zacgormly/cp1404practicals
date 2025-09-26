"""Gopher Population Simulator"""

from random import randint

NUMBER_OF_YEARS = 10
MIN_PERCENTAGE_BORN = 10
MAX_PERCENTAGE_BORN = 20
MIN_PERCENTAGE_DEAD = 5
MAX_PERCENTAGE_DEAD = 25


def main():
    print("Welcome to the Gopher Population Simulator!")
    initial_population = int(input("Starting population: "))
    original_population = initial_population
    for i in range(NUMBER_OF_YEARS):
        print(f"Year {i + 1}")
        proportion_born = determine_proportion_born()
        number_born = calculate_number_born(proportion_born, original_population)
        proportion_dead = determine_proportion_dead()
        number_dead = calculate_number_dead(proportion_dead, original_population)
        new_population = original_population + number_born - number_dead

        print(f"{int(number_born)} gophers were born. {int(number_dead)} died.")
        print(f"Population: {int(new_population)}")
        original_population = new_population


def determine_proportion_born():
    proportion_born = (randint(MIN_PERCENTAGE_BORN, MAX_PERCENTAGE_BORN) / 100)
    return proportion_born


def calculate_number_born(proportion_born, original_population):
    number_born = proportion_born * original_population
    return number_born


def determine_proportion_dead():
    proportion_dead = (randint(MIN_PERCENTAGE_DEAD, MAX_PERCENTAGE_DEAD) / 100)
    return proportion_dead


def calculate_number_dead(proportion_dead, original_population):
    number_dead = proportion_dead * original_population
    return number_dead


main()
