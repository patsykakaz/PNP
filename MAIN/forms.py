#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives

class AskAboForm(forms.Form):
    GENDER_CHOICES = (
        ('Monsieur', 'Monsieur'),
        ('Madame', 'Madame'),
    )
    gender = forms.ChoiceField(label="intitulé",choices=GENDER_CHOICES)
    nom = forms.CharField(label='Nom', max_length=100, required=True)
    prenom = forms.CharField(label='Prénom', max_length=50, required=True)
    email = forms.EmailField(label="Adresse e-mail",required=True)
    societe= forms.CharField(label='société', max_length=50, required=False)
    REVUE_CHOICES = (
        ('PNP', 'PNP'),
        ('La Lettre PNP', 'La Lettre PNP'),
        ('PNP + La Lettre PNP', 'PNP + La Lettre PNP'),
    )
    revue = forms.ChoiceField(choices=REVUE_CHOICES)

    def clean(self):
        email = self.cleaned_data.get('email')
        gender = self.cleaned_data.get('gender')
        nom = self.cleaned_data.get('nom')
        revue = self.cleaned_data.get('revue')
        try:
            subject= "Votre demande abonnement a bien été prise en compte"
            from_email= settings.ADMINS[1][1]
            to = email
            text_content = "Bonjour "+ str(gender) +" "+ str(nom) +". Votre demande d’abonnement à "+ str(revue) + "a bien été prise en compte. Notre service abonnement va prendre contact avec vous très rapidement afin de finaliser votre demande. D’ici là, pour toutes questions, vous pouvez nous joindre aux coordonnées suivantes : Groupe MBC - Service Abonnement ,20 place de l’Horloge,84 000 Avignon,Mail : abonnement@groupembc.com,Tel : 04 90 14 61 41.   Cordialement, L’équipe MBC. "
            html_content = "<p>Bonjour "+ str(gender) +" "+ str(nom) +"</p><p>Votre demande d’abonnement à <strong>"+ str(revue) +"</strong> a bien été prise en compte.</p> <p>Notre service abonnement va prendre contact avec vous très rapidement afin de finaliser votre demande. </p><p>D’ici là, pour toutes questions, vous pouvez nous joindre aux coordonnées suivantes : </p><p>Groupe MBC - Service Abonnement <br />20 place de l’Horloge <br />84 000 Avignon <br />Mail : abonnement@groupembc.com <br />Tel : 04 90 14 61 41 <br /></p>Cordialement, <br />L’équipe MBC."
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            self.add_error('email', '')
            raise forms.ValidationError("L'adresse mail soumise semble invalide")
        return self.cleaned_data


