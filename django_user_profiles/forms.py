from django import forms
from django.contrib.auth import authenticate
from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput # <input type='password' />
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Пользователь с таким именем уже существует'
            )




class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                raise forms.ValidationError(
                    "Неверный логин или пароль"
                )

        return cleaned_data