from datetime import datetime
from colorama import Fore, Style
from password_checker import (
    check_password_strength, 
    check_common_password, 
    simulate_dictionary_attack, 
    simulate_brute_force_attack
)
from password_personal_info import check_personal_info


def generate_recommendations(issues, is_common, personal_info_issue):
    recommendations = []


    for issue in issues:
        match issue:
            case "Password should be at least 8 characters long.":
                recommendations.append(f"{Fore.YELLOW}Use a password that is at least 8 characters long.{Style.RESET_ALL}")
            case "Password should contain at least one lowercase letter.":
                recommendations.append(f"{Fore.YELLOW}Include at least one lowercase letter in your password.{Style.RESET_ALL}")
            case "Password should contain at least one uppercase letter.":
                recommendations.append(f"{Fore.YELLOW}Include at least one uppercase letter in your password.{Style.RESET_ALL}")
            case "Password should contain at least one digit.":
                recommendations.append(f"{Fore.YELLOW}Include at least one digit in your password.{Style.RESET_ALL}")
            case "Password should contain at least one special character.":
                recommendations.append(f"{Fore.YELLOW}Include at least one special character in your password.{Style.RESET_ALL}")

    if not issues:
        recommendations.append(f"{Fore.GREEN}Your password is strong. Here are some general tips for maintaining password security:{Style.RESET_ALL}")
        recommendations.append(f"{Fore.YELLOW} - Avoid using the same password for multiple accounts.{Style.RESET_ALL}")
        recommendations.append(f"{Fore.YELLOW} - Change your passwords regularly.{Style.RESET_ALL}")
        recommendations.append(f"{Fore.YELLOW} - Use a password manager to generate and store unique passwords.{Style.RESET_ALL}")
        recommendations.append(f"{Fore.YELLOW} - Avoid using easily guessable information like names, dates, or common words.{Style.RESET_ALL}")


    if is_common:
        recommendations.append(f"{Fore.RED}Avoid using common passwords. Choose a more unique password.{Style.RESET_ALL}")


    if personal_info_issue:
        recommendations.append(f"{Fore.RED}Avoid using personal information like name, DOB, pet name, or place of residence in your password.{Style.RESET_ALL}")

    return recommendations



def generate_report(password, common_passwords, personal_info):
    report = []
    report.append(f"{Fore.CYAN}Password Analysis Report - {datetime.now()}{Style.RESET_ALL}\n")
    report.append(f"{Fore.CYAN}Password: {'*' * len(password)}{Style.RESET_ALL}\n")


    strength, issues = check_password_strength(password)
    if strength == 5:
        report.append(f"{Fore.GREEN}Password Strength: Strong{Style.RESET_ALL}\n")
    elif strength >= 3:
        report.append(f"{Fore.YELLOW}Password Strength: Moderate{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.RED}Password Strength: Weak{Style.RESET_ALL}\n")


    if issues:
        report.append(f"{Fore.RED}Issues found:{Style.RESET_ALL}\n")
        for issue in issues:
            report.append(f"{Fore.RED} - {issue}{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.GREEN}No issues found.{Style.RESET_ALL}\n")


    if check_common_password(password, common_passwords):
        report.append(f"{Fore.RED}Password is too common.{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.GREEN}Password is not in the list of common passwords.{Style.RESET_ALL}\n")


    personal_info_issue, info = check_personal_info(password, personal_info)
    if personal_info_issue:
        report.append(f"{Fore.RED}Password is similar to personal information: {info}{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.GREEN}Password is not similar to any provided personal information.{Style.RESET_ALL}\n")


    if simulate_dictionary_attack(password, common_passwords):
        report.append(f"{Fore.RED}Password is vulnerable to a dictionary attack.{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.GREEN}Password is not vulnerable to a dictionary attack.{Style.RESET_ALL}\n")


    time_to_crack = simulate_brute_force_attack(password)
    if time_to_crack < 60:
        report.append(f"{Fore.RED}Password can be cracked in less than a minute: {time_to_crack:.2f} seconds{Style.RESET_ALL}\n")
    elif time_to_crack < 3600:
        report.append(f"{Fore.RED}Password can be cracked in less than an hour: {time_to_crack / 60:.2f} minutes{Style.RESET_ALL}\n")
    elif time_to_crack < 86400:
        report.append(f"{Fore.YELLOW}Password can be cracked in less than a day: {time_to_crack / 3600:.2f} hours{Style.RESET_ALL}\n")
    else:
        report.append(f"{Fore.GREEN}Estimated time to crack the password: {time_to_crack / 86400:.2f} days{Style.RESET_ALL}\n")


    recommendations = generate_recommendations(issues, check_common_password(password, common_passwords), personal_info_issue)
    report.append(f"{Fore.CYAN}Recommendations:{Style.RESET_ALL}\n")
    for rec in recommendations:
        report.append(f" - {rec}\n")


    return ''.join(report)