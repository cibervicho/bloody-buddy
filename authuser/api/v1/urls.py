from django.urls import path, include

from authuser.views import pacientes

urlpatterns = [
    path('pacientes', pacientes),
]
