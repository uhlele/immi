from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from . import methods
from .models import ImmiDocument


@api_view(["POST"])
def login(request):
    try:
        data = methods.validate_login_data(request.data)
        return Response(status=status.HTTP_200_OK,
                        data=data)
    except ValidationError as v_error:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'success': False, 'message': str(v_error)})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'success': False, 'message': str(e)})


@api_view(["POST"])
def registration(request):
    try:
        data = methods.validate_registration_details(request.data)
        return Response(status=status.HTTP_200_OK,
                        data = data)
    except ValidationError as v_error:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'success': False, 'message': str(v_error)})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'success': False, 'message': str(e)})

@api_view(["GET"])
def validate_user(request, activation_token):
    print(activation_token)
    activation_token_a = activation_token[0:10]
    activation_token_b = activation_token[10:]
    print(activation_token_a)
    print(activation_token_b)
    try:
        data = methods.activate_user(activation_token_a, activation_token_b)
    except ValidationError as verror:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'success': False, 'message': str(verror)})
    if data:
        return Response(status=status.HTTP_200_OK,
                        data={'success': True, 'message' : "User Activated" })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'success': True, "message": "Activation Error"})

@api_view(["POST"])
def upload(request):
    ImmiDocument.objects.create(name=request.FILES.get("file"))
    return Response(status=status.HTTP_200_OK, data={'success': True, 'message' : "File uploaded" })
