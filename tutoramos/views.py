from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken






def get_tokens(user: User) -> dict:
    refresh = RefreshToken.for_user(user)

    return {
        'tokens': {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    }
