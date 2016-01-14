#-*- coding: utf-8 -*-
from time import strftime

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

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if str(ABM_TEST_MAIL(username)) != '00':
            msg=''
            self.add_error('username', msg)
            self.add_error('password', msg)
            raise forms.ValidationError("Adresse email inexistante.")
        aboAuthResult = authenticateByEmail(username,password)
        if aboAuthResult != 'true':
            msg = ''
            self.add_error('password', msg)
            raise forms.ValidationError("Mot de passe incorrect.")
        return self.cleaned_data

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]


class MailModifForm(forms.Form):
    mail = forms.CharField(label='Adresse mail', widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super(MailModifForm, self).clean()
        # TODO -> ovveride mail regex (No default ".tld" verification)
        mail = self.cleaned_data.get('mail')
        mailExist = ABM_TEST_MAIL(mail)
        mailExist = str(mailExist)
        if mailExist == '00':
            msg='adresse mail invalide'
            self.add_error('mail', msg)
            raise forms.ValidationError("Adresse mail déjà présente en base de données.")
        elif mailExist != '01':
            msg='Adresse mail rejetée'
            self.add_error('mail', msg)
            raise forms.ValidationError("ABM_TEST_MAIL return failed")
        try:
            subject= 'MODIFICATION ADRESSE MAIL - pnpapetier.com'
            from_email=settings.ADMINS[0][1]
            toHash = str(mail) + strftime("%d/%m/%Y")
            text_content = "Veuillez trouver ci-après le code de vérification pour changer votre adresse mail: " + b64encode(sha1(toHash).digest())[:6]
            html_content = "<p>Veuillez trouver ci-après le code de vérification pour changer votre adresse mail: <br/> <b>" + b64encode(sha1(toHash).digest())[:6] + "</b> </p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [mail])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            msg = ""
            self.add_error('mail', msg)
            raise forms.ValidationError("L'envoi d'email à l'adresse %s a échoué." % str(mail))
        return self.cleaned_data

class MailConfirmationForm(forms.Form):
    code_verification = forms.CharField(max_length=255, help_text='Entrez le code de vérification qui vous a été envoyé sur l\'adresse mail renseignée à l\'étape précédente.')
    confirmation_mail = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        code = self.cleaned_data.get('code_verification')
        mail = self.cleaned_data.get('confirmation_mail')
        if not b64encode(sha1(mail+strftime('%d/%m/%Y')).digest())[:6] == code:
            msg=''
            self.add_error('code_verification', msg)
            raise forms.ValidationError("Code de vérification incorrect.")
        return self.cleaned_data


class PasswordModifForm(forms.Form):
    password1 = forms.CharField(label='mot de passe', help_text='6 caractères minimum', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirmation', help_text='Entrez le même mot de passe qu\'au dessus', widget=forms.PasswordInput)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            msg=''
            self.add_error('password1', msg)
            self.add_error('password2', msg)
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        elif len(password1) < 6:
            msg=''
            self.add_error('password1', msg)
            self.add_error('password2', msg)
            raise forms.ValidationError("Mot de passe trop court. Veuillez entrer un mot de passe d'au moins 6 caractères")
        return self.cleaned_data
