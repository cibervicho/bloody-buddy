from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from authuser.models import User
from authuser.serializers import PatientSerializer, PatientModelSerializer

# Create your views here.
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