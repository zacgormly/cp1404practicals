"""My Guitars Program"""

from guitar import Guitar

GUITARS_CSV = "guitars.csv"


def main():
    """Program to load and display guitars from CSV."""
    guitars = load_guitars()
    print_guitars(guitars)
    # Test __lt__ method
    print(f"__lt__ test, Expected True, Got: {guitars[1] < guitars [0]}")
    print(f"__lt__ test, Expected False, Got: {guitars[3] < guitars[2]}")
    print(f"__lt__ test, Expected False, Got: {guitars[4] < guitars[5]}")


def print_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def load_guitars():
    guitars = []
    with open("%s" % GUITARS_CSV, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


main()
