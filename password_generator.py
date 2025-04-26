import random
import pyperclip  # Optional, for copying to clipboard

# Define character pools
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

# Ask user for input
length = int(input("Enter the desired password length: "))
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Build character pool based on user selection
character_pool = ""
if include_upper:
    character_pool += uppercase
if include_lower:
    character_pool += lowercase
if include_numbers:
    character_pool += numbers
if include_special:
    character_pool += special_characters

# Check if the character pool is empty
if not character_pool:
    print("You must select at least one character type!")
else:
    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))

    # Display password
    print(f"Generated password: {password}")

    # Optional: Copy to clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard.")
