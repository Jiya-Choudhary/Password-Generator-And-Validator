import random
import string

class PasswordError(Exception):
    pass
def generate_password(Length= 12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_characters)
    for _ in range(Length))
    return password

user_password=input("Enter password:")
try:
    if len(user_password)<8:
        raise PasswordError("Password is too short , It must contain more than 8 words")
    if not any (char.isdigit() for char in user_password):
        raise PasswordError("Your password must contain numeric value")
    print("Valid Password")
except PasswordError as error:
    print(f"Rejected:{error}")

