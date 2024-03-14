import re
def is_valid_username(username):
    return username.isalpha()

def is_valid_password(password):
    if len(password) < 7:
        return False
    if not any(char.isdigit() for char in password):
        return False
    special_characters = r'@_!#$%^&*()?/\|}{~:'
    if not any(char in special_characters for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    
    return True

def main():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if is_valid_username(username) and is_valid_password(password):
        print("You have logged into the system.")
    else:
        print("Authentication failed. Please check the rules for username and password.")

if __name__ == "__main__":
        main()