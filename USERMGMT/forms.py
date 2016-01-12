#-*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from base64 import b64encode
from hashlib import sha1

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
        # TODO -> ovveride mail regex (No default ".tld" verification)
        mail = self.cleaned_data.get('mail')
        mailExist = ABM_TEST_MAIL(mail)
        mailExist = str(mailExist)
        if mailExist == '00':
            raise forms.ValidationError("Adresse mail déjà présente en base de données.")
        elif mailExist != '01':
            raise forms.ValidationError("ABM_TEST_MAIL return failed")
        try:
            subject='MODIFICATION MOT DE PASSE - pnpapetier.com'
            from_email='n.burton@groupembc.com'
            to = mail
            text_content = "Veuillez trouver ci-après le code de vérification pour changer votre adresse mail: "+str(b64encode(sha1(mail).digest()))
            html_content = "<p>Veuillez trouver ci-après le code de vérification pour changer votre adresse mail: <br/> <b>" + str(b64encode(sha1(mail).digest())) + "</b> </p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            raise forms.ValidationError("L'envoi d'email à l'adresse %s a échoué." % str(mail))
        return self.cleaned_data

class MailConfirmationForm(forms.Form):
    code_verification = forms.CharField(max_length=255, help_text='Entrez le code de vérification qui vous a été envoyé sur l\'adresse mail renseignée à l\'étape précédente.')


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
