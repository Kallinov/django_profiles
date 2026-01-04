from django.apps import AppConfig
from .settings import auto_profile_create


class DjangoUserProfilesConfig(AppConfig):
    name = 'django_user_profiles'
    label = 'profiles'

    if auto_profile_create:
        def ready(self):
            import django_user_profiles.signals
            return super().ready()
