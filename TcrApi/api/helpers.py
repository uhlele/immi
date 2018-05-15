import uuid
#import secrets
import hashlib
import string
import random

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def convert_password_to_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def generate_random_key(): 
    alphabet = string.ascii_letters + string.digits
    key = ''.join(random.choice(alphabet) for _ in range(10))
    return key
