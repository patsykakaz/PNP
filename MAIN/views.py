#-*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import *

from .models import *


from pysimplesoap.client import SoapClient

get_backends()

def test(request):

    client = SoapClient(wsdl="http://dev.aboweb.com/aboweb/ClientService?wsdl", ns="web", trace=False)
    client['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'mbc2015'}
    bob = {'codeClient':0,'typeClient':'0','nom':'bob2', 'prenom':'bobby2', 'cp':'75011', 'email':'test2@test.test'}
    result = client.createOrUpdateClientEx(client=bob)

    k = authenticate(username='test@test.test', password='test')
    login(request, k)
    return HttpResponse("result is -> {} <br /> user.is_staff = {}".format(result, k.is_staff))

def get_client(request):

    client = SoapClient(wsdl="http://dev.aboweb.com/aboweb/ClientService?wsdl", ns="web", trace=False)
    client['AuthHeaderElement'] = {'Login': 'admin.webservices@mbc.com', 'Password': 'MBC1475'}
    txt = client.getNbClients
    return HttpResponse(txt)



@login_required
def req(request):
    print 'login is required for this view'
    return HttpResponse('superOK')

def kill(request):
    logout(request)
    return HttpResponse('logged out')

def get_db_archive(request):
    from db_PNP import DB
    txt = ""
    i=0
    for item in DB:
        content = item[4]
        k = Archive(title=item[2].decode('utf-8'),content=content.decode('utf-8'))
        k.save()
    # txt = txt.decode('utf-8')

    return HttpResponse(k.title)

