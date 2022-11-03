from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path('create_user', views.CreateUser.as_view()),
    path('update_user', views.UpdateUser.as_view()),
    path('password', views.UpdatePassword.as_view()),
    path('get_user/<int:pk>', views.Get_n_Dele.as_view()),
    path('login', views.Login.as_view()),
    path('jwt/create', TokenObtainPairView.as_view()),
    path('jwt/refresh', TokenRefreshView.as_view()),
    path('jwt/verify',  TokenVerifyView.as_view()),
]
