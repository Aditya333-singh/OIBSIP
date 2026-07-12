import random
import string

def generate_password():
    print("--- Random Password Generator ---")
    
    # 1. Get password length from user
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # 2. Get user preferences for character types
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Build the pool of characters
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # 3. Generate password
    if not char_pool:
        print("You must select at least one character type!")
    else:
        password = ''.join(random.choice(char_pool) for _ in range(length))
        print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    generate_password()