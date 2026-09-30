import random

print("Password Generator")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if length < 4:
    print("Password length must be at least 4.")

elif length > 100:
    print("Password length must not exceed 100.")

else:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "@#$%&*!"

    password = ""

    password += random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(numbers)
    password += random.choice(special)

    all_characters = lowercase + uppercase + numbers + special

    for i in range(length - 4):
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)

    password = "".join(password_list)

    print("Generated Password:", password)