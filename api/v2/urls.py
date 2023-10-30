# To be used with Django Rest-Framework
from django.urls import path

from api.views import (
    getProfiles,
    getProfile,
    getBloodPressures,
    getBloodPressure,
    getMedicalNotes,
    getMedicalNote,
    getWeights,
    getWeight,

    LoginView,
    LogoutView,
    ListUsersView,
    PatientsView
)

urlpatterns = [
    path('profiles', getProfiles, name='get_profiles'),
    path('profiles/<str:pk>', getProfile, name='get_profile'),
    
    path('pressures', getBloodPressures, name='get_blood_pressures'),
    path('pressures/<str:pk>', getBloodPressure, name='get_blood_pressure'),

    path('medicalnotes', getMedicalNotes, name='get_medical_notes'),
    path('medicalnotes/<str:pk>', getMedicalNote, name='get_medical_note'),

    path('weights', getWeights, name='get_weights'),
    path('weights/<str:pk>', getWeight, name='get_weight'),



    path('auth/login', LoginView.as_view(), name='auth_login'),
    path('auth/logout', LogoutView.as_view(), name='auth_logout'),
    path('usuarios', ListUsersView.as_view(), name='list_users'),
    path('pacientes', PatientsView.as_view(), name='patients_view')
]
