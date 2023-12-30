import secrets
import string
import math

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True, author=None):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Create a pool of characters based on complexity settings
    pool = lowercase_letters
    if use_uppercase:
        pool += uppercase_letters
    if use_digits:
        pool += digits
    if use_symbols:
        pool += symbols

    # Generate the password
    password = ''.join(secrets.choice(pool) for _ in range(length))

    # Calculate password strength percentage
    complexity_count = sum([use_uppercase, use_digits, use_symbols])
    strength_percentage = (complexity_count / 3) * 100

    # Calculate the number of possible combinations
    num_combinations = len(pool) ** length

    # Estimate the time to crack (assuming 1 billion attempts per second)
    seconds_to_crack_guessing = num_combinations / 1_000_000  # 1 million attempts per second (for guessing)
    seconds_to_crack_tools = num_combinations / 1_000_000_000  # 1 billion attempts per second (for cracking tools)
    minutes_to_crack_guessing = seconds_to_crack_guessing / 60
    hours_to_crack_guessing = minutes_to_crack_guessing / 60
    days_to_crack_guessing = hours_to_crack_guessing / 24
    months_to_crack_guessing = days_to_crack_guessing / 30
    years_to_crack_guessing = days_to_crack_guessing / 365
    minutes_to_crack_tools = seconds_to_crack_tools / 60
    hours_to_crack_tools = minutes_to_crack_tools / 60
    days_to_crack_tools = hours_to_crack_tools / 24
    months_to_crack_tools = days_to_crack_tools / 30
    years_to_crack_tools = days_to_crack_tools / 365

    # Return password and strength information
    return password, f"{strength_percentage:.2f}%", years_to_crack_guessing, months_to_crack_guessing, days_to_crack_guessing, years_to_crack_tools, months_to_crack_tools, days_to_crack_tools, author

# Example usage
password, strength, years_guessing, months_guessing, days_guessing, years_tools, months_tools, days_tools, author = generate_password(length=20, use_uppercase=True, use_digits=True, use_symbols=True, author="Safi Ullah Khan")
print(f"Generated Password: {password}")
print(f"Password Strength: {strength} strong")
print(f"Time to Crack by Guessing (years): {years_guessing:.2f} years, {months_guessing:.2f} months, {days_guessing:.2f} days")
print(f"Time to Crack by Tools (years): {years_tools:.2f} years, {months_tools:.2f} months, {days_tools:.2f} days")
print(f"Author: {author}")
