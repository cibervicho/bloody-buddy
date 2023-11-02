# To be used with Django Rest-Framework
from rest_framework import serializers

from authuser.models import User, Profile
# from bloodpressurerecord.models import BloodPressureRecord
# from medicalnote.models import MedicalNote
# from weightrecord.models import Weight


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'


# class BloodPressureSerializer(serializers.ModelSerializer):
#     owner = ProfileSerializer(many=False)
#     class Meta:
#         model = BloodPressureRecord
#         fields = '__all__'


# class MedicalNoteSerializer(serializers.ModelSerializer):
#     owner = ProfileSerializer(many=False)
#     class Meta:
#         model = MedicalNote
#         fields = '__all__'


# class WeightSerializer(serializers.ModelSerializer):
#     owner = ProfileSerializer(many=False)
#     class Meta:
#         model = Weight
#         fields = '__all__'







class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'last_name', 'password', 'is_active',
                  'is_superuser', 'is_staff', 'date_joined')



# class PatientSerializer(serializers.ModelSerializer):
#     #https://stackoverflow.com/questions/43031323/how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model
#     id = serializers.IntegerField(read_only=True)
#     email = serializers.EmailField(required=True, allow_null=False)
#     password = serializers.CharField(required=True, allow_null=False, write_only=True)
#     name = serializers.CharField(required=True, allow_null=False)
#     last_name = serializers.CharField(required=True, allow_null=False)
#     birth_date = serializers.DateField()
#     gender = serializers.CharField()
#     is_doctor = serializers.BooleanField(required=True, allow_null=False)

#     class Meta:
#         model = User
#         fields = ('id','email','password','name','last_name','birth_date','gender','is_doctor')
    
#     def create(self, validated_data):
#         user = super(PatientSerializer, self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
