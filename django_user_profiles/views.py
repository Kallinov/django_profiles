from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from .models import Profile, User
from .forms import RegisterForm, LoginForm

class RegisterFormView(FormView):
    template_name = 'profiles/registration.html'
    form_class = RegisterForm
    success_url = '/profiles/users/all'

    def form_valid(self, form):
        data = form.cleaned_data
        u = User(username=data['username'])
        u.set_password(data['password'])
        u.save()

        login(self.request, u)
        return super().form_valid(form)
    
class LoginFormView(FormView):
    template_name = 'profiles/login.html'
    form_class = LoginForm
    success_url = '/profiles/users/all'

    def form_valid(self, form):
        data = form.cleaned_data
        u = authenticate(
            username=data['username'],
            password=data['password']
        )

        login(self.request, u)
        return super().form_valid(form)
    

def index(request):
    p = Profile.objects.all()

    return render(request, 'profiles/index.html', {'profiles': p})
    
    
def all_users(request):
    u = User.objects.all()
    return render(request, 'profiles/all_users.html', {'users': u})

def get_profile(request, id):

    p = Profile.objects.filter(user_id=id)

    if not p:
        return HttpResponse('404 Not Found')

    return render(request, 'profiles/profile.html', {'profile': p.get(), 'user': request.user})
