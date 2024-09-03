from termcolor import colored
from colorama import init, Style
from password_common import load_common_passwords
from password_personal_info import get_personal_info, get_password
from password_report import generate_report



def main():
    init(autoreset=True)
    common_passwords = load_common_passwords('common_passwords.txt')
    personal_info = get_personal_info()
    password = get_password()
    report = generate_report(password, common_passwords, personal_info)
    print("\n" + report)



if __name__ == "__main__":
    main()
