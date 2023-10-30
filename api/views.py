from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from authuser.models import User, Profile
from bloodpressurerecord.models import BloodPressureRecord
from medicalnote.models import MedicalNote
from weightrecord.models import Weight

from api.serializers import (
    ProfileSerializer,
    BloodPressureSerializer,
    MedicalNoteSerializer,
    WeightSerializer,

    UserSerializer,
    ListUserModelSerializer,
    PatientSerializer,
    PatientModelSerializer,
)

# Create your views here.

##     ##  #######  
##     ## ##     ## 
##     ##        ## 
##     ##  #######  
 ##   ##  ##        
  ## ##   ##        
   ###    ######### 

### authuser.profile ###
@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    profile = get_object_or_404(Profile,pk=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)



### bloodpressurerecord ###
@api_view(['GET'])
def getBloodPressures(request):
    bprs = BloodPressureRecord.objects.all()
    serializer = BloodPressureSerializer(bprs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBloodPressure(request, pk):
    bpr = get_object_or_404(BloodPressureRecord,pk=pk)
    serializer = BloodPressureSerializer(bpr, many=False)
    return Response(serializer.data)



### medicalnote ###
@api_view(['GET'])
def getMedicalNotes(request):
    medical_notes = MedicalNote.objects.all()
    serializer = MedicalNoteSerializer(medical_notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMedicalNote(request, pk):
    medical_note = get_object_or_404(MedicalNote,pk=pk)
    serializer = MedicalNoteSerializer(medical_note, many=False)
    return Response(serializer.data)



### weightrecord ###
@api_view(['GET'])
def getWeights(request):
    weights = Weight.objects.all()
    serializer = WeightSerializer(weights, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeight(request, pk):
    weight = get_object_or_404(Weight, pk=pk)
    serializer = WeightSerializer(weight, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def setWeight(request, pk):
    weight = get_object_or_404(Weight, pk=pk)
    user = request.user.profile
    data = request.data

    print('DATA:', data)

    serializer = WeightSerializer(weight, many=False)
    return Response(serializer.data)





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
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")



##     ##    ##   
##     ##  ####   
##     ##    ##   
##     ##    ##   
 ##   ##     ##   
  ## ##      ##   
   ###     ###### 

@login_required
def v1_profiles(request):
    profiles = Profile.objects.all()

    result = []
    for profile in profiles:
        p = {
            'full_name': profile.full_name,
            'email': profile.user.email,
            'birth_date': profile.birth_date,
            'gender': profile.gender,
        }
        result.append(p)
    
    return JsonResponse(
        {
            'data': result,
            'code': 200,
            'message': 'ok'
        }
    )


