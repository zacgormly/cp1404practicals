"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    print()

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    income_report = generate_report(incomes, number_of_months)
    print_report(income_report)


def generate_report(incomes, number_of_months):
    """Generate report values and store in tuple."""
    report = []
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        report.append((month, income, total))
    return report

def print_report(income_report):
    """Print report."""
    print("\nIncome Report\n-------------")
    for month, income, total in income_report:
        print(f"Month {month:2} - Income: ${income:10.2f} \t\t\t Total: ${total:10.2f}")


main()