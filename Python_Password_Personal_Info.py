from termcolor import colored
from itertools import permutations



def print_header(text, level):
    if level == 1:
        print(colored(text, "cyan", attrs=['bold', 'underline']))  
    elif level == 2:
        print(colored(text, "green", attrs=['bold']))  



def generate_combinations(personal_info):
    combinations_list = []

    for length in range(1, len(personal_info) + 1):
        for combo in permutations(personal_info, length):
            combined = ''.join(combo)
            combinations_list.append(combined)
            combinations_list.append(combined.lower())
            combinations_list.append(combined.upper())
            combinations_list.append(combined.capitalize())

    return combinations_list



def get_personal_info():
    print_header("Welcome to the Password Analyzer!", 1)
    print_header("Please enter the following personal information:", 2)

    name = input(colored("Enter your name: ", "yellow"))
    dob = input(colored("Enter your date of birth (DDMMYYYY): ", "yellow"))
    email = input(colored("Enter your email address: ", "yellow"))
    phone_number = input(colored("Enter your phone number: ", "yellow"))

    optional_fields = [
        "pet's name", "place you live", "favorite movie", "favorite singer",
        "favorite movie character", "favorite song", "favorite anime", "favorite series",
        "favorite number", "favorite character name", "food", "quote", "favorite dialogue",
        "favorite actor", "favorite anime character", "favorite series character", "favorite movie character"
    ]

    personal_info = {
        "name": name,
        "dob": dob,
        "email": email,
        "phone_number": phone_number
    }

    for field in optional_fields:
        response = input(colored(f"Would you like to provide your {field}? (yes/no): ", "yellow")).strip().lower()
        if response == 'yes':
            personal_info[field] = input(colored(f"Enter your {field}: ", "yellow"))

    return personal_info



def get_password():
    return input(colored("Enter a password to generate a report: ", "yellow"))



def check_personal_info(password, personal_info):
    combined_info = generate_combinations(personal_info)
    for info in combined_info:
        if info in password:
            return True, info
        
    return False, None
