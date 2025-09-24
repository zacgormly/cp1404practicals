"""More Scores"""

from random import randint


def main():
    """Write specified number of scores with performance to results file."""
    number_of_scores = int(input("Number of scores: "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        random_score = randint(0, 100)
        performance = determine_performance(random_score)
        print(f"{random_score} is {performance}", file=out_file)
    out_file.close()


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
