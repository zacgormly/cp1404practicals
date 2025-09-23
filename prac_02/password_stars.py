"""Password Validator"""


def main():
    """Validate and mask password."""
    min_length = 3
    symbol = "."
    password = get_password(min_length)
    print_asterisks(password, symbol)


def print_asterisks(password, symbol="*"):
    """Print asterisks as many times as password length."""
    print(symbol * len(password))


def get_password(min_length):
    """Get a password of valid length."""
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid password length.")
        password = input("Password: ")
    return password


main()
