import random

print("Welcome to Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789"

number = int(input("Amount of passwords to generate: "))

length = int(input("Enter your password length: "))
print("Here are your passwords:")

for password in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)
    