# To be used with Django Rest-Framework
from django.urls import path, include

from authuser.views import (
    LoginView,
    LogoutView,
    ListUsersView,
    PatientsView,
    #v2_pacientes
)

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='auth_login'),
    path('auth/logout', LogoutView.as_view(), name='auth_logout'),
    path('usuarios', ListUsersView.as_view(), name='list_users'),
    path('pacientes', PatientsView.as_view(), name='patients_view')
]
