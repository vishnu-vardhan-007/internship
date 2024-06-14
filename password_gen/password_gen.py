import random
import string


def generate_password(length):
    """Generate a single random password with the given length."""
    if length < 4:
        raise ValueError(
            "Password length must be at least 4 characters to include all character types.")

    # Define the possible characters in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one of each character type
    password = [
        random.choice(lower),  # Lowercase
        random.choice(upper),  # Uppercase
        random.choice(digits),  # Digit
        random.choice(special)  # Special character
    ]

    # Fill the rest of the password length with a random selection of all character types
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)


def generate_passwords(length, count):
    """Generate a list of random passwords."""
    return [generate_password(length) for _ in range(count)]


def main():
    # User instructions
    print("Welcome to the Password Generator!")
    print("Please follow the instructions below to generate secure passwords.")

    # Get user input for password length and number of passwords
    while True:
        try:
            length = int(
                input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an integer of at least 4.")

    while True:
        try:
            count = int(input("Enter the number of passwords to generate: "))
            if count <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate and display the passwords
    passwords = generate_passwords(length, count)
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"{i}: {password}")


if __name__ == "__main__":
    main()
