import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Password Generator")
size = int(input("Enter password length: "))
pwd = generate_password(size)
print("Your password is:", pwd)
