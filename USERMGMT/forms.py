#-*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Adresse mail', widget=forms.EmailInput)
    password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]

class UserModif(forms.Form):
    mail = forms.CharField(label='Adresse mail', widget=forms.EmailInput)
    password1 = forms.CharField(label='mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmation mot de passe', widget=forms.PasswordInput)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")

        return self.cleaned_data