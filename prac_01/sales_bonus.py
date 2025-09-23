"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_THRESHOLD = 1000
SMALL_BONUS = 0.1
LARGE_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = SMALL_BONUS
    else:
        bonus_rate = LARGE_BONUS
    bonus_amount = sales * bonus_rate
    print(f"Bonus is ${bonus_amount}")
    sales = float(input("Enter sales: $"))
print("Finished")