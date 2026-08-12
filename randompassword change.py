
import string
import secrets

def generate_secure_password(length=16):
    """Generates a secure, random password of a given length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters for the general pool
    all_characters = lower + upper + digits + symbols

    while True:
        # Generate a random password from the full pool
        password = ''.join(secrets.choice(all_characters) for _ in range(length))
        
        # Enforce complexity requirements
        has_lower = any(char in lower for char in password)
        has_upper = any(char in upper for char in password)
        has_digits = any(char in digits for char in password)
        has_symbols = any(char in symbols for char in password)
        
        # Return the password only if it meets all criteria
        if has_lower and has_upper and has_digits and has_symbols:
            return password

# Example usage
if __name__ == "__main__":
    generated_password = generate_secure_password(16)
    print(f"Generated Password: {generated_password}")