MINIMUM_PASSWORD_LENGTH = 10

password = input(f"Make a password (minimum {MINIMUM_PASSWORD_LENGTH} characters):  ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password is not long enough!")
    password = input(f"Make a password (minimum {MINIMUM_PASSWORD_LENGTH} characters):  ")
print("*" * len(password))