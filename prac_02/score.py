"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

RANDOM_LOW_LIMIT = 0
RANDOM_HIGH_LIMIT = 100


def main():
    score = float(input("Enter score: "))
    result = determine_performance(score)
    print(result)

    random_score = randint(RANDOM_LOW_LIMIT, RANDOM_HIGH_LIMIT)
    random_result = determine_performance(random_score)
    print(f"Random score is: {random_score}.")
    print(random_result)


def determine_performance(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()
