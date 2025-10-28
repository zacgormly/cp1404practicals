"""
Wimbledon
Estimate: 40 minutes
Actual:   60 minutes
"""

WIMBLEDON_DATA = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Load, process and display results of Wimbledon champions and countries."""
    lines = load_wimbledon_data()
    champion_to_win_count, unique_countries = process_wimbledon_data(lines)
    print_results(champion_to_win_count, unique_countries)


def print_results(champion_to_win_count, unique_countries):
    """Print the Wimbledon champions with a win count and countries that have won."""
    print("Wimbledon Champions:")
    for champion, win_count in champion_to_win_count.items():
        print(champion, win_count)
    print()
    print(f"These {len(unique_countries)} countries have won Wimbledon:")
    print(', '.join(sorted(unique_countries)))


def process_wimbledon_data(lines):
    """Create champion to win count dictionary and countries set."""
    champion_to_win_count = {}
    countries = set()
    for items in lines:
        champion, country = items[CHAMPION_INDEX], items[COUNTRY_INDEX]
        champion_to_win_count[champion] = champion_to_win_count.get(champion, 0) + 1
        countries.add(country)
    return champion_to_win_count, countries


def load_wimbledon_data():
    """Load data from Wimbledon csv file and store as list of lists."""
    lines = []
    with open(WIMBLEDON_DATA, encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip data header
        for line in in_file:
            items = line.strip().split(',')
            lines.append(items)
    return lines


main()
