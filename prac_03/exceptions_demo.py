"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. When the user inputs an incorrect datatype, such as string, into either numerator or denominator integer input.
# 2. When the user inputs a 0 integer into the denominator, as you cannot divide by zero.
# 3. Yes. This can be done by adding an indefinite loop to validate if the user's input is 0 or not for the denominator
# variable. This must be done before the variable's value is passed to the fraction calculation to avoid the ZeroDivisionError.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0, as you cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")