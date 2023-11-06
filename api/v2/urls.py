# To be used with Django Rest-Framework
from django.urls import path

from api.views import (
    UsersList, UsersDetail, UsersCreate,
    BloodPressureList, BloodPressureDetail, BloodPressureCreate,
    NotesList, NotesCreate, NotesDetail,
    WeightList, WeightCreate, WeightDetail,
    
    ## Leaving these here for reference.
    #LoginView, LogoutView,
    #ListUsersView, DetailUsersView,
)

urlpatterns = [
    ## Leaving these here for reference.
    # path('auth/login', LoginView.as_view(), name='auth_login'),
    # path('auth/logout', LogoutView.as_view(), name='auth_logout'),
    # path('usuarios', ListUsersView.as_view(), name='list_users'),
    # path('usuarios/<int:pk>', DetailUsersView.as_view(), name='detail_users'),

    path('usuarios', UsersList.as_view(), name='list_users'),
    path('usuarios/', UsersList.as_view(), name='list_users'),
    path('usuarios-create', UsersCreate.as_view(), name='list_users'),
    path('usuarios-create/', UsersCreate.as_view(), name='list_users'),
    path('usuarios/<int:pk>', UsersDetail.as_view(), name='detail_users'),
    path('usuarios/<int:pk>/', UsersDetail.as_view(), name='detail_users'),

    path('usuarios/<int:pk>/pressures', BloodPressureList.as_view(), name='list_pressures'),
    path('usuarios/<int:pk>/pressures/', BloodPressureList.as_view(), name='list_pressures'),
    path('usuarios/<int:pk>/pressures-create', BloodPressureCreate.as_view(), name='create_pressures'),
    path('usuarios/<int:pk>/pressures-create/', BloodPressureCreate.as_view(), name='create_pressures'),
    path('usuarios/pressures/<int:pk>', BloodPressureDetail.as_view(), name='detail_pressures'),
    path('usuarios/pressures/<int:pk>/', BloodPressureDetail.as_view(), name='detail_pressures'),

    path('usuarios/<int:pk>/notes', NotesList.as_view(), name='list_notes'),
    path('usuarios/<int:pk>/notes/', NotesList.as_view(), name='list_notes'),
    path('usuarios/<int:pk>/notes-create', NotesCreate.as_view(), name='create_notes'),
    path('usuarios/<int:pk>/notes-create/', NotesCreate.as_view(), name='create_notes'),
    path('usuarios/notes/<int:pk>', NotesDetail.as_view(), name='detail_notes'),
    path('usuarios/notes/<int:pk>/', NotesDetail.as_view(), name='detail_notes'),

    path('usuarios/<int:pk>/weights', WeightList.as_view(), name='list_weights'),
    path('usuarios/<int:pk>/weights/', WeightList.as_view(), name='list_weights'),
    path('usuarios/<int:pk>/weights-create', WeightCreate.as_view(), name='create_weights'),
    path('usuarios/<int:pk>/weights-create/', WeightCreate.as_view(), name='create_weights'),
    path('usuarios/weights/<int:pk>', WeightDetail.as_view(), name='detail_weights'),
    path('usuarios/weights/<int:pk>/', WeightDetail.as_view(), name='detail_weights'),
]
