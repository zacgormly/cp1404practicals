"""
Emails
Estimate: 30 minutes
Actual:   24 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if not (confirmation == "" or confirmation == "y"):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name(email):
    username = email.split('@')[0]
    name_parts = username.split('.')
    name = ' '.join(name_parts).title()
    return name


main()
