from django.db import models
from django.contrib.auth.models import User # Default user model.
                                            # You can change it to your custom model
from django.db.models import F
from .settings import default_avatar, default_visibility

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creater_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    display_name = models.CharField(max_length=20, blank=True)
    bio = models.CharField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default=default_avatar)
    birth_date = models.DateField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)

    is_public = models.BooleanField(default=default_visibility)
    show_email = models.BooleanField(default=True)
    show_social_links = models.BooleanField(default=True)

    def save(self, *args, **kwargs): # Default value for display_name
        if not self.display_name:
            self.display_name = f"user{self.user.id}"

        super().save(*args, **kwargs)