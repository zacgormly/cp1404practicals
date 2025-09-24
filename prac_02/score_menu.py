"""Main Menu"""

MENU = ("(G)et valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    """Menu to get and display name."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            performance = determine_performance(score)
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get valid score between 0 and 100 inclusive."""
    score = int(input("score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("score: "))
    return score


def print_line(length):
    """Print line of hyphens."""
    print('-' * length)


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
