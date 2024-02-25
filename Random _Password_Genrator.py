# The lines `import secrets` and `import string` in the Python code are importing modules that provide additional functionality to the script.
import secrets
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    The function `generate_password` creates a random password of a specified length using a combination
    of letters, numbers, and symbols based on user preferences.
    """
    if not length:
        return "Error: Password length must be greater than 0."

    if not (use_letters or use_numbers or use_symbols):
        return "Error: At least one character type must be selected."

    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "Error: No character types selected. Please try again."

    password = ""
    for _ in range(length):
        password += secrets.choice(character_set)

    return password

def main():
    """
    The main function prompts the user to input desired password length and preferences for including
    letters, numbers, and symbols, then generates a password based on the input.
    
    """
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password (minimum 12): "))
    if length < 12:
        print("Error: Password must be at least 12 characters long.")
        return

    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password.startswith("Error: "):
        print(password)
    else:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()