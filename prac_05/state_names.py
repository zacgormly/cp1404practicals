"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
MAX_STATE_CODE_LENGTH = 3

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3} is {state_name}")

is_invalid = False
while not is_invalid:
    try:
        state_code = input("Enter short state: ").upper()
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
