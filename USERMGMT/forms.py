#-*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from MAIN.webservices import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Adresse mail', widget=forms.EmailInput)
    password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]


class MailModifForm(forms.Form):
    mail = forms.CharField(label='Adresse mail', widget=forms.EmailInput)

    def clean(self):
        # ovveride mail regex (No default ".xx" verification)
        mail = self.cleaned_data.get('mail')
        mailExist = ABM_TEST_MAIL(mail)
        mailExist = str(mailExist)
        if mailExist == '00':
            raise forms.ValidationError("Adresse mail déjà présente en base de donnée.")
        elif mailExist != '01' :
            raise forms.ValidationError("ABM_TEST_MAIL return failed")
        return self.cleaned_data

class PasswordModifForm(forms.Form):
    password1 = forms.CharField(label='mot de passe', help_text='6 caractères minimum', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmation', help_text='Entrez le même mot de passe qu\'au dessus', widget=forms.PasswordInput)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        elif len(password1) < 6:
            raise forms.ValidationError("Mot de passe trop court. Veuillez entrer un mot de passe d'au moins 6 caractères")
        return self.cleaned_data
