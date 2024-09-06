import hashlib
import getpass
import pickle

# File to store user data
DATA_FILE = 'user_data.pkl'

# Load user data from file
def load_data():
    try:
        with open(DATA_FILE, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

# Save user data to file
def save_data(data):
    with open(DATA_FILE, 'wb') as file:
        pickle.dump(data, file)

# Hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create a new account
def create_account(user_data):
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists!")
        return
    
    password = getpass.getpass("Enter a password: ")
    hashed_password = hash_password(password)
    user_data[username] = hashed_password
    save_data(user_data)
    print("Account created successfully!")

# Login to an existing account
def login(user_data):
    username = input("Enter your username: ")
    if username not in user_data:
        print("Username not found!")
        return
    
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)
    if user_data[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid password!")

# Main function with a menu for user interaction
def main():
    user_data = load_data()
    
    while True:
        print("\nPassword Manager")
        print("1. Create Account")
        print("2. Login")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account(user_data)
        elif choice == '2':
            login(user_data)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
