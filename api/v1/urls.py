from django.urls import path

from api.views import v1_profiles

urlpatterns = [
    path('profiles', v1_profiles),
]
