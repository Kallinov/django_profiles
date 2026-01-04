# django-profiles

django-profiles is a Django app that extends the normal
functionality of the user model by adding profiles


Quick start
-----------

1. Add "profiles" to your INSTALLED_APPS setting like this:
    ```
    INSTALLED_APPS = [
        ...,
        "django_profiles.apps.DjangoUserProfilesConfig",
    ]
    ```

2. Add the MEDIA_ROOT and MEDIA_URL in settings.py of your site like this:
    ```
    MEDIA_ROOT = BASE_DIR / 'media/'

    MEDIA_URL = '/media/'
    ```

4. Include the profiles URLconf in your project urls.py and add path for images (DEBUG=True) like this:
    ```
    path("profiles/", include("django_simple_feedback.urls")),
    ```
    ```
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

3. Run ```python manage.py migrate``` to create the models.

4. Start the development server and visit the admin to create a feedback.

5. Visit the ```profiles/<int:id>``` URL to see the profile for user whose id=id.
