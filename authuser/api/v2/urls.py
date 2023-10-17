# To be used with Django Rest-Framework
from django.urls import path, include

from authuser.views import v2_pacientes

urlpatterns = [
    path('', v2_pacientes),
]
