#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class AskAboForm(forms.Form):
    GENDER_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    nom = forms.CharField(label='Nom', max_length=100, required=True)
    prenom = forms.CharField(label='prenom', max_length=50, required=True)
    email = forms.EmailField(required=True)
    societe= forms.CharField(label='société', max_length=50, required=False)

    def clean(self):
        try:
            # send mail()
            pass
        except:
            self.add_error('email', '')
            raise forms.ValidationError("L'adresse mail soumise semble invalide")
        return self.cleaned_data