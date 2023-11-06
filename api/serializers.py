# To be used with Django Rest-Framework
from rest_framework import serializers

from authuser.models import User, Profile
from bloodpressurerecord.models import BloodPressureRecord
from medicalnote.models import MedicalNote
from weightrecord.models import Weight


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        #fields = '__all__'
        exclude = ('owner',)
        read_only_fields = ['creation_date']


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        #fields = '__all__'
        exclude = ('owner',)
        read_only_fields = ['creation_date']


class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressureRecord
        # fields = '__all__'
        exclude = ('owner',)
        read_only_fields = ['creation_date']


class ProfileSerializer(serializers.ModelSerializer):
    pressure_records_count = serializers.SerializerMethodField(read_only=True)
    weigth_records_count = serializers.SerializerMethodField(read_only=True)
    medical_notes_count = serializers.SerializerMethodField(read_only=True)

    def get_pressure_records_count(self, owner):
        return owner.pressure_records.count()

    def get_weigth_records_count(self, owner):
        return owner.pesos.count()

    def get_medical_notes_count(self, owner):
        return owner.notas_paciente.count()

    class Meta:
        model = Profile
        fields = ('full_name', 'birth_date', 'gender', 'user_type', 'creation_date',
                  'pressure_records_count', 'medical_notes_count', 'weigth_records_count')
        read_only_fields = ['full_name', 'creation_date']


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'last_name', 'password', 'profile',
                  'is_active', 'is_superuser', 'is_staff', 'date_joined')
        read_only_fields = ['id', 'profile', 'is_active', 'is_superuser',
                            'is_staff', 'date_joined']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_joined = serializers.DateTimeField(read_only=True)
    
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'last_name', 'profile',
                  'is_active', 'is_superuser', 'is_staff',
                  'date_joined')
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()

        full_name = f"{validated_data.get('last_name', instance.last_name)} {validated_data.get('name', instance.name)}"
        profile.full_name = full_name
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.user_type = profile_data.get('user_type', profile.user_type)
        profile.save()

        return instance
