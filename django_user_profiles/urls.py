from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.get_profile, name='get_profile'),
    path('users/register/', views.RegisterFormView.as_view(), name='register'),
    path('users/login/', views.LoginFormView.as_view(), name='login'),
    path('users/all/', views.all_users, name='all_users'),
]