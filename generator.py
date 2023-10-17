import secrets
import string
import json

# Function to generate a random password
def generate_password(length, include_digits, include_special_chars):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to save a password with associated website and username
def save_password(passwords, website, username, password):
    passwords[website] = {"username": username, "password": password}
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

# Function to auto-fill a password
def auto_fill_password(passwords, website):
    if website in passwords:
        info = passwords[website]
        print(f"Auto-filling for {website}:")
        print(f"Username: {info['username']}")
        print(f"Password: {info['password']}")
    else:
        print(f"No stored password found for {website}.")

# Main program
if __name__ == "__main__":
    passwords = {}
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        pass

    while True:
        print("Password Generator")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Auto-fill Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            include_digits = input("Include digits (y/n)? ").lower() == "y"
            include_special_chars = input("Include special characters (y/n)? ").lower() == "y"
            password = generate_password(length, include_digits, include_special_chars)
            print(f"Generated Password: {password}")

        elif choice == "2":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(passwords, website, username, password)
            print(f"Password for {website} saved.")

        elif choice == "3":
            website = input("Enter website for auto-fill: ")
            auto_fill_password(passwords, website)

        elif choice == "4":
            with open("passwords.json", "w") as file:
                json.dump(passwords, file, indent=4)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
