from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def create_jwt(User):
    refresh = RefreshToken.for_user(User)

    token = {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }

    return token
