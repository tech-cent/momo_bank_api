import re

def is_phonenumber_valid(phone_number: str) -> bool:
    """
    Checks if phone number is valid
    """
    if not(len(phone_number)) == 12:
        return False
    if re.match('[2][5][6]+', phone_number) == None:
        return False
    return True
