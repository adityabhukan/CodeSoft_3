import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with specified complexity.
    
    Parameters:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Combine all allowed characters
    all_chars = lowercase + uppercase + digits + special
    
    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the rest with random choices from all allowed characters
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def get_user_input():
    """
    Get password requirements from user input.
    
    Returns:
        tuple: (length, use_uppercase, use_digits, use_special)
    """
    print("=== Password Generator ===")
    
    # Get password length
    while True:
        try:
            length = int(input("Enter password length (8-64): "))
            if 8 <= length <= 64:
                break
            print("Please enter a number between 8 and 64.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return (length, use_uppercase, use_digits, use_special)

def main():
    # Get user requirements
    length, use_uppercase, use_digits, use_special = get_user_input()
    
    # Generate password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    
    # Display the password
    print("\nGenerated Password:")
    print(password)
    
    # Strength indicator (simple version)
    strength = "Weak"
    if length >= 12 and use_uppercase and use_digits and use_special:
        strength = "Strong"
    elif length >= 10 and (use_uppercase or use_digits or use_special):
        strength = "Medium"
    
    print(f"\nPassword Strength: {strength}")

if __name__ == "__main__":
    main()
