from .models import ImmiUser
from .email_service import send_email
from .helpers import generate_random_key


def validate_user(email, password):
    if ImmiUser.objects.filter(email=email).exists():
        if ImmiUser.objects.filter(email=email,
                                 password=password).exists():
            if ImmiUser.objects.filter(email=email).values_list(
                    'is_approved',
                    flat=True)[0]:
                user_details = ImmiUser.objects.get(email=email)
                return {"user_type": user_details.user_type.name,
                        "user_id": user_details.id,
                        "first_name": user_details.first_name,
                        "success": True}
            else:
                return {"error": "Oops!!This User is not Approved",
                        "success": False}
        else:
            return {"error": "Oops!! email and Password do not match",
                    "success": False}
    else:
        return {"error": "Oops!! This email do not exist", "success": False}


def register_user(email, password, first_name, last_name):
    if ImmiUser.objects.filter(email=email).exists():
        return {"error": "Oops!! This email already exists", "success": False}
    else:
        activation_key_a = generate_random_key()
        activation_key_b = generate_random_key()
        user_dict = {"first_name": first_name, "last_name": last_name,
                "password": password, "email": email, "activation_token_a" : activation_key_a, "activation_token_b" : activation_key_b}
        register_user = ImmiUser.objects.create(**user_dict)
        activation_url = "localhost:8000/api/activate_user/{}".format(activation_key_a + activation_key_b)
        send_email(email, "Please confirm your emailid by clicking at: {}".format(activation_url))
        return user_dict['email']

def activate_user(activation_token_a, activation_token_b):
    if ImmiUser.objects.filter(activation_token_a=activation_token_a, activation_token_b=activation_token_b).exists():
        ImmiUser.objects.filter(activation_token_a=activation_token_a, activation_token_b=activation_token_b).update(is_active=True)
        return True
    else:
        return False


