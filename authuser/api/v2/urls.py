# To be used with Django Rest-Framework
from django.urls import path, include

from authuser.views import (
    LoginView,
    LogoutView,
    v2_pacientes
)

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='auth_login'),
    path('auth/logout', LogoutView.as_view(), name='auth_logout'),
    path('pacientes', v2_pacientes),
]