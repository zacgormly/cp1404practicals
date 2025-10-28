"""
Emails
Estimate: 30 minutes
Actual:   24 minutes
"""


def main():
    """Program to create a dictionary of emails to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = determine_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if not (confirmation == "" or confirmation.upper() == "Y"):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name(email):
    """Determine possible name from email."""
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name


main()
