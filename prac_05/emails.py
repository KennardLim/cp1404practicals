"""
Emails
Estimate: 30 minutes
Actual: 25 minutes
"""
email_to_name = dict()

def main():
    """Asks the user for emails of users and stores them with their username before printing each user and their respective email"""
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        choice = input(f"Is your name {name} (Y/n) ").lower()
        if choice == "y" or choice == "":
            email_to_name[email] = name
        else:
            name = input("Name: ")
            email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extracts the username from an email"""
    name = email.split("@")
    name = name[0].title().split(".")
    name = " ".join(name)
    return name

main()