from django.urls import path

from authuser.views import v1_pacientes

urlpatterns = [
    path('pacientes', v1_pacientes),
]
