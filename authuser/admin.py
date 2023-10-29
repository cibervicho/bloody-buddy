from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Doctor

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmacion de Password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        #fields = ["email", "date_of_birth"]
        fields = ["email",]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Los Passwords son distintos")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "name", "last_name", "birth_date",
                  "gender", "is_doctor", "is_active", "is_superuser", "is_staff"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    search_fields = ['email']
    list_display = ['email', 'name', 'last_name']
    ordering = ['email']
    filter_horizontal = ['groups', 'user_permissions']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Información Personal', {'fields': [
            'name',
            'last_name',
            'birth_date',
            'gender',
            'is_doctor'
        ]}),
        ('Permisos', {'fields': [
            'is_active',
            'is_staff',
            'is_superuser'
        ]}),
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None, 
            {
                'classes': ['wide'],
                'fields': ['email', 'name', 'last_name', 'birth_date',
                           'gender', 'password1', 'password2'],
            }
        ),
    ]


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Doctor)