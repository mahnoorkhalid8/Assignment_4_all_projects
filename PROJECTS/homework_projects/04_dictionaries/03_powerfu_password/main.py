import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_login = {
    "password@example.com" : hash_password("password123"),
    "user@example.com" : hash_password("xyz1234")
}

def login(email, password):
    if email in stored_login:
        return stored_login[email] == hash_password(password)
    return False

def main():
    email = input("Enter email: ")
    password = input("Enter password: ")

    if login(email, password):
        print("You're successfully logged in!!!")
    else:
        print("Invalid email or password!")

if __name__ == "__main__":
    main()