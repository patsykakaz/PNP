#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from mezzanine.utils.urls import login_redirect, next_url
from mezzanine.pages.models import Page
from .models import *
from forms import *

from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *

get_backends()

# base64.b64encode(hashlib.sha1("MBC2015").digest())
# >>> 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw='
# base64.b64encode(hashlib.sha1("MBC1475").digest())
# >>> 'pYsIJKF18hj0SvS3TwrQV3hWzD4='

def ask_abo(request):
    if request.POST:
        form = AskAboForm(request.POST)
        if form.is_valid():
            subject= "DEMANDE ABONNEMENT - "+ request.POST['revue']
            from_email= settings.ADMINS[1][1]
            to = "philippe@lesidecar.fr"
            text_content = "Une nouvelle demande d'abonnement vient d'être soumise sur pnpapetier.com pour le(s) magazine(s) : "+ request.POST['revue'] +". Les informations sont les suivantes : "+ request.POST['gender'] +" (prénom) "+ request.POST['prenom']+" (nom)"+ request.POST['nom'] +" (société)"+ request.POST['societe'] +". Email = "+ request.POST['email']
            html_content = "<p>Une nouvelle demande d'abonnement vient d'être soumise sur pnpapetier.com pour le(s) magazine(s) : "+ request.POST['revue'] +".</p> <p>Les informations sont les suivantes : </p> genre = "+ request.POST['gender'] +"<br /> prénom = "+ request.POST['prenom']+"<br /> nom = "+ request.POST['nom'] +"<br /> société = "+ request.POST['societe'] +" <br /> Email = "+ request.POST['email']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            message = "Votre demande a bien été prise en compte. Un mail vous a été adressé."
        else:
            form = AskAboForm(request.POST)
            error = "Données soumises invalides..."
    else:
        message = "PAGE EN COURS DE DEVELOPPEMENT"
        form = AskAboForm()
    return render(request, 'abonnement.html', locals())

def kill(request):
    logout(request)
    return HttpResponseRedirect('/')

def archive(request,start,end):
    from django.contrib.sites.models import Site
    from mezzanine.blog.models import BlogPost
    from db_PNP import DB
    
    start,end = int(start), int(end)

    site = Site.objects.get(name='LA LETTRE')

    for item in DB[start:end]:
        content = item[4].decode('utf-8').replace('src="','src="/archives/')
        u = item[17]
        u = u.split(',')
        u = u[0].split(':')
        u = u[1].replace('"','').replace('\\','')
        if len(u) > 3:
            u = 'archives/'+u
        else:
            u = None
        if item[8] != "0000-00-00 00:00:00":
            k = BlogPost(site=site,
                        user_id=1,
                        title=item[2].decode('utf-8'),
                        content=content,
                        featured_image=u,
                        publish_date=item[8],
                        archive=True
                        )
        else: 
            k = BlogPost(site=site,
                        user_id=1,
                        title=item[2].decode('utf-8'),
                        content=content,
                        featured_image=u,
                        publish_date=item[15],
                        archive=True
                        )
            print item[15]
        k.save()
    return HttpResponse("archiving process ended.")





