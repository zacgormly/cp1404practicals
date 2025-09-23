"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """Score and performance program."""
    score = float(input("Enter score: "))
    result = determine_performance(score)
    print(result)

    random_score = randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_performance(random_score)
    print(f"Random score is: {random_score}.")
    print(random_result)


def determine_performance(score):
    """Determine performance based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()
