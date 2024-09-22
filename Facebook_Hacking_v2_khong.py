import itertools
import string
import time

# Function to simulate login process (checking if the password matches the correct one)
def login_with_password(password):
    # Replace this with the actual login process that checks the password
    # For example, you could use selenium to automate the login process
    # and return True if the login was successful, False otherwise
    return False

# Function to generate all possible combinations of letters, digits, and symbols for 8 characters
def brute_force_password():
    # Define the set of characters to use (A-Z, a-z, 0-9, and symbols)
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?"
    
    # Generate all possible 8-character combinations (brute-force)
    for attempt in itertools.product(characters, repeat=8):
        # Join tuple to create string
        password = ''.join(attempt)
        
        # Simulate typing the password (printing it)
        print(f"Trying password: {password}")
        
        # Wait for 0.5 seconds (faster typing)
        time.sleep(0.5)
        
        # Simulate pressing 'Enter' (reduced delay)
        time.sleep(0.5)
        
        # Check if the password matches the correct one
        if login_with_password(password):
            print(f"Correct password found: {password}")
            return password
        
        # If login is incorrect, simulate deleting each character with backspace
        print("Incorrect password. Deleting each character with backspace...")
        for _ in range(len(password)):
            time.sleep(0.01)  # Reduced delay between backspaces
        
        # Wait for a shorter time before typing the next password
        time.sleep(0.1)  # Reduced waiting time before writing the next password
        
    print("No valid password found.")
    return None

# Input for the user to enter their Facebook account
facebook_account = input("Please enter your Facebook account: ")

# Call the brute-force password function
found_password = brute_force_password()

if found_password:
    print(f"Login successful with password: {found_password}")
else:
    print("Failed to find the correct password.")
