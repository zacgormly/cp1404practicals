"""
CP1404/CP5632 Practical
State names in a dictionary
File has been reformatted and inputs are no longer case-sensitive
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}
MAX_STATE_CODE_LENGTH = 3

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:{MAX_STATE_CODE_LENGTH}} is {state_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
