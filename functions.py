# Here we create the helper functions for the controllers

import bcrypt
import re

def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode()

def hash_verify(password, hashed_password):
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, hashed_password.encode())
    return result



# how to check length of a password
def is_valid_password(password, min_len=8, max_len=64):
    return min_len <= len(password) <= max_len
# check if emaail is valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None