def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        common_passwords = file.read().splitlines()
        
    return common_passwords
