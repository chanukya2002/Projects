import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the length for each password: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    for i in range(num_passwords):
        password = generate_password(password_length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()
