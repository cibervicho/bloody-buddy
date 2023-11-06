from django.urls import path

from api.views import v1_profiles

urlpatterns = [
    path('usuarios', v1_profiles),
]
