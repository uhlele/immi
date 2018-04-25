from datetime import datetime, timedelta

import re
from . import db
from . import helpers


def validate_login_data(data):
    email = data['email']
    password = data['password']
    password_md5 = helpers.convert_password_to_md5(password)
    data = db.validate_user(email, password_md5)
    return data

def validate_registration_details(data):
    if data['email'] and data['password']:
        return db.register_user(data['email'],data['password'],data['first_name'],data['last_name'])
    else:
        return False

def activate_user(activation_token_a, activation_token_b):
    return db.activate_user(activation_token_a, activation_token_b)
