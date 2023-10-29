from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import (
    User,
    Profile,
)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        print("  --> Creating a PROFILE automatically for user", user.name)
        profile = Profile.objects.create(
            user = user,
            full_name = f'{user.name} {user.last_name}',
            user_type = 'P', # We default to 'patiente'
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    print("  --> Deleting the USER", user.name, "automatically")
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)