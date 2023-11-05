from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from authuser.models import User, Profile
from bloodpressurerecord.models import BloodPressureRecord
# from medicalnote.models import MedicalNote
from weightrecord.models import Weight

from api.serializers import (
    BloodPressureSerializer,
    # MedicalNoteSerializer,
    WeightSerializer,

    UserSerializer, UserCreateSerializer,
)

# Create your views here.

##     ##  #######  
##     ## ##     ## 
##     ##        ## 
##     ##  #######  
 ##   ##  ##        
  ## ##   ##        
   ###    ######### 


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




class WeightCreate(generics.CreateAPIView):
    serializer_class = WeightSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        owner = Profile.objects.get(pk=pk)

        serializer.save(owner=owner)


class WeightList(generics.ListAPIView):
    serializer_class = WeightSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Weight.objects.filter(owner=pk)


class WeightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer




class BloodPressureCreate(generics.CreateAPIView):
    serializer_class = BloodPressureSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        owner = Profile.objects.get(pk=pk)

        serializer.save(owner=owner)


class BloodPressureList(generics.ListAPIView):
    serializer_class = BloodPressureSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return BloodPressureRecord.objects.filter(owner=pk)


class BloodPressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodPressureRecord.objects.all()
    serializer_class = BloodPressureSerializer




class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(pk=pk)
    
    def perform_destroy(self, instance):
        """Deletes a single user object"""

        try:
            # Since we have a signal that takes care of the automatic deletion
            # of the User, we just delete the Profile.
            pk = self.kwargs.get('pk')
            user = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'Usuario eliminado satisfactoriamente'}, status=status.HTTP_204_NO_CONTENT)


## Leaving these here for reference.
# class ListUsersView(APIView):
#     def get(self, request):
#         """Returns a list of users"""

#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")

#         try:
#             users = User.objects.all()
#         except User.DoesNotExist:
#             return Response({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)

#         serialized_users = UserSerializer(users, many=True).data
#         return Response(serialized_users, status=status.HTTP_200_OK)


#     def post(self, request):
#         """Creates a new user into the User and Profile models
        
#         Example:
#         {
#             "email": "olivia@hotmail.com",
#             "name": "Olivia",
#             "last_name": "Rodrigo",
#             "password": "Per30rito"
#         }
#         """

#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")

#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


# class DetailUsersView(APIView):
#     def get(self, request, pk):
#         """Returns a single user object"""

#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")

#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         serialized_user = UserSerializer(user, many=False).data
#         return Response(serialized_user, status=status.HTTP_200_OK)


#     def patch(self, request, pk):
#         """Updates a single user object
        
#         Example1:
#         {
#             "profile": {
#                 "gender": "M"
#             }
#         }

#         Example2:
#         {
#             "email": "test2@outlook.com",
#             "profile": {}
#         }
#         """

#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")

#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         serialized_user = UserSerializer(user, data=request.data, partial=True)
#         if serialized_user.is_valid():
#             serialized_user.save()
#             return Response(serialized_user.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         """Deletes a single user object"""

#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")

#         try:
#             # Since we have a signal that takes care of the automatic deletion
#             # of the User, we just delete the Profile.
#             user = Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         user.delete()
#         return Response({'message': 'Usuario eliminado satisfactoriamente'}, status=status.HTTP_204_NO_CONTENT)




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


