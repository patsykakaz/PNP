#-*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import *

get_backends()

# def test(request):
#     user = request.user
#     if user : 
#         return HttpResponse(user)
#     else: 
#         return HttpResponse("OK")

def test(request):

    from pysimplesoap.client import SoapClient

    client = SoapClient(wsdl="http://dev.gesmag.com:8080/aboweb/abmWeb?wsdl", ns="web", trace=True)
    client['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'mbc2015'}
    result = client.ADM_ACCES_BASE(600,99,99)


    k = authenticate(username='test@test.test', password='test')
    login(request, k)
    return HttpResponse("result is -> {} <br /> user.is_staff = {}".format(result, k.is_staff))

@login_required
def test_login_req(request):
    return HttpResponse('superOK')
