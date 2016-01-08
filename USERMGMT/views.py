#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from mezzanine.utils.urls import login_redirect, next_url
from forms import *

from MAIN.webservices import *

get_backends()

def connect(request):
    error = False
    if request.GET:
        articleAttempt = True
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return login_redirect(request)
            else:
                error = "Echec de l'authentification"
                return render(request, 'login.html', locals())
    else:
        form = LoginForm()
    return render(request, 'login.html', locals())

def killUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def showUser(request):
    display = True
    if request.POST:
        form = UserModifForm(request.POST)
        if form.is_valid:
            print "ok"
    else:
        form = UserModifForm()
    return render(request, 'login.html', locals())

@login_required
def changeUser(request):
    modification = True
    if request.POST:
        currentForm = False
        if 'modification_mail' in request.POST:
            print "MODIF MAIL"
            currentForm = MailModifForm
        elif 'modification_password' in request.POST:
            print "MODIF PASSWORD"
            currentForm = PasswordModifForm
        else:
            raise ValueError('changerUser POST dict do not contain the required values')
        form = currentForm(request.POST)
        if form.is_valid():
            # DO CHANGE HERE
            user = getClient(request.user.username)
            if currentForm == MailModifForm: 
                try:
                    user.email = form.cleaned_data['mail']
                    createOrUpdateClientEx(user)
                    user = User.objects.get(username=request.user.username)
                    user.email = form.cleaned_data['mail']
                    user.save()
                    message = 'Adresse mail modifié avec succès.'
                except:
                    raise IOError('user.mail update has failed')
            elif currentForm == PasswordModifForm:
                try:
                    user.motPasseAbm = form.cleaned_data['password1']
                    createOrUpdateClientEx(user)
                    message = 'Mot de passe modifié avec succès.'
                except:
                    raise IOError('user.motPasseAbm update has failed')
        else:
            if currentForm == MailModifForm:
                form1 = MailModifForm(request.POST)
                form2 = PasswordModifForm()
            else:
                form1 = MailModifForm()
                form2 = PasswordModifForm(request.POST)
    form1 = MailModifForm()
    form2 = PasswordModifForm()
    return render(request, 'modificationUser.html', locals())

@login_required
def test_log_req(request):
    return HttpResponse('LOGIN REQUIRED IS SATISFIED')



