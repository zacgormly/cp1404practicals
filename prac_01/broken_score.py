"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    performance = "Invalid score"
elif score < 50:
    performance = "Bad"
elif score < 90:
    performance = "Passable"
else:
    performance = "Excellent"
print(f"Your score is considered: {performance}")
