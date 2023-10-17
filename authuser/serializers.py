# To be used with Django Rest-Framework
from rest_framework import serializers

from authuser.models import User

class PatientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    birth_date = serializers.DateField()
    gender = serializers.CharField()
    is_doctor = serializers.BooleanField()