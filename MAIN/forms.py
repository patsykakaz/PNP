#-*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Adresse mail', widget=forms.EmailInput)
    password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)