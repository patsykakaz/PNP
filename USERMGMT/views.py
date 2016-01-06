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
from forms import *

from MAIN.webservices import *

get_backends()

def connect(request):
    error = False
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
                error = True
                return render(request, 'login.html', locals())
    else:
        form = LoginForm()
    return render(request, 'login.html', locals())

def killUser(request):
    logout(request)
    return HttpResponseRedirect('/')

def showUser(request):
    display = True
    if request.POST:
        form = UserModif(request.POST)
        if form.is_valid:
            print "ok"
    else:
        form = UserModif()
    return render(request, 'login.html', locals())

@login_required
def test_log_req(request):
    return HttpResponse('LOGIN REQUIRED IS SATISFIED')


