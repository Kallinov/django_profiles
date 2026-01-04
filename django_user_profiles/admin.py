from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'user__email', 'is_public']

    list_filter = ['is_public']

    search_fields = ['display_name', 'user__email']


admin.site.register(Profile, ProfileAdmin)