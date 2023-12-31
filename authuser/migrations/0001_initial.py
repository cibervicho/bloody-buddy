# Generated by Django 4.2.5 on 2023-10-29 06:50

import authuser.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=500, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Apellidos')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Ingreso')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Ultimo ingreso')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', authuser.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Completo')),
                ('birth_date', models.DateField(blank=True, default=datetime.date(1900, 1, 1), verbose_name='Fecha de Nacimiento')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Genero')),
                ('user_type', models.CharField(blank=True, choices=[('A', 'Administrador'), ('P', 'Paciente'), ('M', 'Medico')], max_length=1, null=True, verbose_name='Tipo de Usuario')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Creacion')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
