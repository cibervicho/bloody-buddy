from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.db import models
from django.utils import timezone

from datetime import date


# Create your models here.
# The instructions to reach this were taken from the YouTube channel: CodeWithStein


# Overriding the UserManager with our own functionality
class CustomUserManager(UserManager):
    """Helps Django work with our custom user model."""

    # Help function to save a new into the DB
    def _create_user(self, email, password, **extra_fields):
        """Helper function to create users in teh system."""

        if not email:
            raise ValueError("You have not provided a valid email address")

        if not password:
            raise ValueError("You have not provided a valid password")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    # Function to create a normal user
    def create_user(self, email=None, password=None, **extra_fields):
        """Creates a new user profile object."""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)


    # Function to create a super user
    def create_superuser(self, email=None, password=None, **extra_fields):
        """Creates and saves a new superuser profile object."""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)


# Constructing the Doctor model
#class Doctor(models.Model):
#    name = models.CharField(max_length=255, blank=True, default='',
#                            verbose_name='Nombre')
#    last_name = models.CharField(max_length=255, blank=True, default='',
#                                 verbose_name='Apellidos')
#    speciality = models.CharField(max_length=100, verbose_name='Especialidad',
#                                   blank=True, null=True)
#
#    class Meta:
#        verbose_name = 'Doctor'
#        verbose_name_plural = 'Doctors'
#
#    def get_full_name(self):
#        return f'{self.name} {self.last_name}'
#
#    def get_short_name(self):
#        return self.name or self.email.split('@')[0]


# Constructing the User Model
class User(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user' object in the system."""

    email = models.EmailField(max_length=500, blank=True, default='',
                              unique=True)
    name = models.CharField(max_length=255, blank=True, default='',
                            verbose_name='Nombre')
    last_name = models.CharField(max_length=255, blank=True, default='',
                                 verbose_name='Apellidos')

    # Field to indicate a user of the system is a doctor (later)
    #is_doctor = models.BooleanField(default=False, verbose_name='Es doctor?')

    #doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True,
    #                           null=True, related_name='patients')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now,
                                       verbose_name='Fecha de Ingreso')
    last_login = models.DateTimeField(blank=True, null=True,
                                      verbose_name='Ultimo ingreso')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """How the 'user' object is shown to the world."""

        return self.get_full_name()
    
    def get_full_name(self):
        """Used to get a users full name"""

        return f'{self.last_name}, {self.name}'

    def get_short_name(self):
        """Used to get a users short name"""

        return self.name or self.email.split('@')[0]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True, 
                            verbose_name='Nombre Completo')
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento',
                                  blank=True, default=date(1900, 1, 1))
    GENDER_CHOICES = [
        ('M', 'Mujer'),
        ('H', 'Hombre'),
        ('O', 'Otro'),
    ]
    gender = models.CharField(max_length=1, blank=True, null=True,
                              choices=GENDER_CHOICES, verbose_name='Genero')
    USER_TYPE_CHOICES = [
        ('A', 'Administrador'),
        ('P', 'Paciente'),
        ('M', 'Medico'),
    ]
    user_type = models.CharField(max_length=1, blank=True, null=True,
                                 choices=USER_TYPE_CHOICES,
                                 verbose_name='Tipo de Usuario')
    creation_date = models.DateTimeField(default=timezone.now,
                                         verbose_name='Fecha de Creacion')
    
    #weight_median = models.FloatField(default=0.0, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.get_full_name()}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    

    #@property
    #def getMedianWeight(self):
    #    pass