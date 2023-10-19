from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from authuser.models import User
from authuser.serializers import PatientSerializer, PatientModelSerializer

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        # Borramos la informacion de sesion
        logout(request)

        return Response(status=status.HTTP_200_OK)


def pacientes(request):
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


@api_view(['GET', 'POST'])
def v2_pacientes(request):
    if request.method == 'GET':
        patients = User.objects.all()
        serialized_patients = PatientModelSerializer(patients, many=True)

        return Response(serialized_patients.data)

    else:
        serialized_patients = PatientSerializer(request.data)
        print(serialized_patients)