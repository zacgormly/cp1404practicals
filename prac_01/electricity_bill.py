"""Electricity Bill Estimator"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

daily_kwh_use = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
daily_bill = daily_kwh_use * tariff
overall_bill = daily_bill * number_of_billing_days
print(f"Estimated bill: ${overall_bill:.2f}")