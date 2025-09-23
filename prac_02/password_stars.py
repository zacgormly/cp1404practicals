"""Password Validator"""

min_length = 3
password = input("Password: ")
while len(password) < min_length:
    print("Invalid password length.")
    password = input("Password: ")
print("*" * len(password))