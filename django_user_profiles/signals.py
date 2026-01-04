from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from .settings import auto_profile_create

User = get_user_model()

if auto_profile_create:
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs): # Creates profile after user was created
        if created:
            Profile.objects.create(user=instance)

@receiver(post_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    if instance.avatar:
       instance.avatar.delete(save=False)