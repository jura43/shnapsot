import re

def username_checker(username):
    """
    Verify if 'username' contains anything other than letters and numbers
    Returns True if string contains anything other than letters or numbers
    """

    check = re.search(r'[^A-Za-z0-9]', username) is None

    return not check