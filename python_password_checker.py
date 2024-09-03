import re
from termcolor import colored



def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password should be at least 8 characters long.")
    if not re.search(r"[a-z]", password):
        issues.append("Password should contain at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        issues.append("Password should contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        issues.append("Password should contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Password should contain at least one special character.")

    strength = 5 - len(issues)

    return strength, issues



def check_common_password(password, common_passwords):
    return password in common_passwords



def simulate_dictionary_attack(password, common_passwords):
    return password in common_passwords



def simulate_brute_force_attack(password):
    charset = (
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '0123456789'
        '!@#$%^&*(),.?":{}|<>'
    )
    possible_combinations = len(charset) ** len(password)
    time_to_crack_seconds = possible_combinations / 1_000_000_000

    return time_to_crack_seconds


