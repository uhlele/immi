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

def validate_servie_create_data(data):
    if data['emial'] and data['service_name']:
        return db.create_service(data['email'], data['service_name'])

def activate_user(activation_token_a, activation_token_b):
    return db.activate_user(activation_token_a, activation_token_b)

def approve_payment(data):
    if data['email'] and data['service_request_number'] and data['amount']:
        return db.approve_payment(data['email'], data['service_request_number'], data['amount'])
