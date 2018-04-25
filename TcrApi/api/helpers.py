import uuid

import hashlib
import secrets
import string

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def convert_password_to_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def generate_random_key(): 
    alphabet = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(alphabet) for i in range(10))
    return random_key