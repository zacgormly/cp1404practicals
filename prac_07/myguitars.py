"""My Guitars Program"""

from guitar import Guitar

GUITARS_CSV = "guitars.csv"


def main():
    """Program to load, display and write guitars to/from CSV."""
    guitars = load_guitars()
    # print_guitars(guitars)
    # run_tests(guitars)
    get_guitar(guitars)
    display_guitars(guitars)
    write_guitars_to_csv(guitars)


def display_guitars(guitars):
    """Display guitars in neat format."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_guitar(guitars):
    """Get guitar from user and append to guitars list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    guitars.sort()


def run_tests(guitars):
    """Test __lt__ method."""
    print(f"__lt__ test, Expected True, Got: {guitars[1] < guitars[0]}")
    print(f"__lt__ test, Expected False, Got: {guitars[3] < guitars[2]}")
    print(f"__lt__ test, Expected False, Got: {guitars[4] < guitars[5]}")


def print_guitars(guitars):
    """Print initial guitars."""
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Load guitars from csv."""
    guitars = []
    with open(GUITARS_CSV, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def write_guitars_to_csv(guitars):
    """Write guitars to csv."""
    with open(GUITARS_CSV, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
