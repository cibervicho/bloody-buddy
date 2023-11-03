# To be used with Django Rest-Framework
from django.urls import path

from api.views import (
    LoginView, LogoutView,
    BloodPressureList, BloodPressureDetail, BloodPressureCreate,
    ListUsersView, DetailUsersView,
    WeightList, WeightCreate, WeightDetail,
)

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='auth_login'),
    path('auth/logout', LogoutView.as_view(), name='auth_logout'),
    
    path('usuarios', ListUsersView.as_view(), name='list_users'),
    path('usuarios/<int:pk>', DetailUsersView.as_view(), name='detail_users'),

    path('usuarios/<int:pk>/pressures', BloodPressureList.as_view(), name='list_pressures'),
    path('usuarios/<int:pk>/pressures-create', BloodPressureCreate.as_view(), name='create_pressures'),
    path('usuarios/pressures/<int:pk>', BloodPressureDetail.as_view(), name='detail_pressures'),

    path('usuarios/<int:pk>/weights', WeightList.as_view(), name='list_weights'),
    path('usuarios/<int:pk>/weights-create', WeightCreate.as_view(), name='create_weights'),
    path('usuarios/weights/<int:pk>', WeightDetail.as_view(), name='detail_weights'),
]
