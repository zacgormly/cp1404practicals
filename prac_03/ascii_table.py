"""ASCII Table"""

LOWER = 33
UPPER = 127

character = input("Enter a character: ")
ascii_code = ord(character)
print(f"The ASCII code for {character} is {ascii_code}")

ascii_code = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while ascii_code < LOWER or ascii_code > UPPER:
    print(f"ASCII Code must be between {LOWER} and {UPPER}!")
    ascii_code = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
character = chr(ascii_code)
print(f"The character for {ascii_code} is {character}")

number_of_columns = int(input("Number of columns: "))
number_of_ascii_codes = 0

for ascii_code in range(LOWER, UPPER + 1):
    print(f"{ascii_code} | {chr(ascii_code)}", end="\t")
    number_of_ascii_codes += 1

    if number_of_ascii_codes % number_of_columns == 0:
        print()
