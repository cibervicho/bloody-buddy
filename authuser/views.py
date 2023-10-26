from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from authuser.models import User
from authuser.serializers import (
    UserSerializer,
    ListUserModelSerializer,
    PatientSerializer,
    PatientModelSerializer,
)

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return Response(UserSerializer(user).data,
                            status=status.HTTP_200_OK)
            
        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        # Borramos la informacion de sesion
        logout(request)

        return Response(status=status.HTTP_200_OK)


class ListUsersView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        users = User.objects.all()
        serialized_users = ListUserModelSerializer(users, many=True).data

        return Response(serialized_users, status=status.HTTP_200_OK)


class PatientsView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")

        patients = User.objects.all()
        #serialized_patients = PatientModelSerializer(patients, many=True)
        serialized_patients = PatientSerializer(patients, many=True)

        return Response(serialized_patients.data)






#################################
@login_required
def v1_pacientes(request):
    pacientes = User.objects.all()

    resultado = []
    for paciente in pacientes:
        p = {
            'name': paciente.name,
            'last_name': paciente.last_name,
            'email': paciente.email,
            'birth_date': paciente.birth_date,
            'gender': paciente.gender,
        }
        resultado.append(p)
    
    return JsonResponse(
        {
            'data': resultado,
            'code': 200,
            'message': 'ok'
        }
    )


