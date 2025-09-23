"""Password Validator"""


def main():
    min_length = 3
    symbol = "."
    password = get_password(min_length)
    print_asterisks(password, symbol)


def print_asterisks(password, symbol="*"):
    print(symbol * len(password))


def get_password(min_length):
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid password length.")
        password = input("Password: ")
    return password


main()
