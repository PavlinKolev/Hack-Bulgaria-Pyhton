from client import Client
from settings import MIN_PASS_LEN


def validate_client(client):
    if type(client) is not Client:
        raise TypeError("Type of client object must be Clinet.")
    return True


def validate_username(username):
    if any(x in username for x in [' ', '   ', '\n']):
        raise ValueError("Username cannot contains white space.")
    return True


def validate_password(password, username):
    if len(password) < MIN_PASS_LEN:
        raise ValueError("Length of password must be at least {} symbols".format(MIN_PASS_LEN))
    if username in password:
        raise ValueError("Your username cannot be substring in your password.")
    no_upper = True
    no_special = True
    no_digit = True
    for letter in password:
        if letter.isupper():
            no_upper = False
        if letter in "!@#$%^&*)(_+-~}{?><:|][,":
            no_special = False
        if letter.isdigit():
            no_digit = False
    if no_upper:
        raise ValueError("Password must have capital letter.")
    if no_special:
        raise ValueError("Password must have special letter.")
    if no_digit:
        raise ValueError("Password must have digit.")
    return True
