from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view

from authuser.models import User, Profile
# from bloodpressurerecord.models import BloodPressureRecord
# from medicalnote.models import MedicalNote
# from weightrecord.models import Weight

from api.serializers import (
    # ProfileSerializer,
    # BloodPressureSerializer,
    # MedicalNoteSerializer,
    # WeightSerializer,

    UserSerializer,
    # ListUserModelSerializer,
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
# @api_view(['GET'])
# def getProfiles(request):
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getProfile(request, pk):
#     profile = get_object_or_404(Profile,pk=pk)
#     serializer = ProfileSerializer(profile, many=False)
#     return Response(serializer.data)



### bloodpressurerecord ###
# @api_view(['GET'])
# def getBloodPressures(request):
#     bprs = BloodPressureRecord.objects.all()
#     serializer = BloodPressureSerializer(bprs, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getBloodPressure(request, pk):
#     bpr = get_object_or_404(BloodPressureRecord,pk=pk)
#     serializer = BloodPressureSerializer(bpr, many=False)
#     return Response(serializer.data)



### medicalnote ###
# @api_view(['GET'])
# def getMedicalNotes(request):
#     medical_notes = MedicalNote.objects.all()
#     serializer = MedicalNoteSerializer(medical_notes, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getMedicalNote(request, pk):
#     medical_note = get_object_or_404(MedicalNote,pk=pk)
#     serializer = MedicalNoteSerializer(medical_note, many=False)
#     return Response(serializer.data)



### weightrecord ###
# @api_view(['GET','POST'])
# def getWeights(request):
#     weights = Weight.objects.all()
#     serializer = WeightSerializer(weights, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getWeight(request, pk):
#     weight = get_object_or_404(Weight, pk=pk)
#     serializer = WeightSerializer(weight, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def setWeight(request, pk):
#     weight = get_object_or_404(Weight, pk=pk)
#     user = request.user.profile
#     data = request.data

#     print('DATA:', data)

#     serializer = WeightSerializer(weight, many=False)
#     return Response(serializer.data)





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
        """Returns a list of users"""

        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            return Response({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)
        
        serialized_users = UserSerializer(users, many=True).data
        return Response(serialized_users, status=status.HTTP_200_OK)


    def post(self, request):
        """Creates a new user into the User and Profile models"""

        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class DetailUsersView(APIView):
    def get(self, request, pk):
        """Returns a single user object"""

        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serialized_user = UserSerializer(user, many=False).data
        return Response(serialized_user, status=status.HTTP_200_OK)


    def put(self, request, pk):
        """Updates a single user object"""

        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serialized_user = UserSerializer(user, data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """Deletes the selected user object"""

        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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


