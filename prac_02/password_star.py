MINIMUM_PASSWORD_LENGTH = 10

def main():
    password = get_password()
    print_into_asterisks(password)

def get_password():
    password = input(f"Make a password (minimum {MINIMUM_PASSWORD_LENGTH} characters):  ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password is not long enough!")
        password = input(f"Make a password (minimum {MINIMUM_PASSWORD_LENGTH} characters):  ")
    return password

def print_into_asterisks(word):
    print("*" * len(word))

main()