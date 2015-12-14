#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from mezzanine.pages.models import Page

from .models import *

from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *

get_backends()


# base64.b64encode(hashlib.sha1("MBC2015").digest())
# >>> 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw='
# base64.b64encode(hashlib.sha1("MBC1475").digest())
# >>> 'pYsIJKF18hj0SvS3TwrQV3hWzD4='


def createOrUpdateClientEx_test_1(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl" 
    client = SoapClient(wsdl = wsdl,
                        # cache = None,
                        # ns="ges",
                        soap_ns="soapenv",
                        trace= True,
                        )
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                # 'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    bob = {'ville': 'PARIS', 'societe': 'FEDERATION FRANCAISE DES', 'adresse1': 'PAPETIERS ET SPECIALISTES', 'cp': '75001', 'adresse2': '12 RUE DES PYRAMIDES', 'nom': 'test', 'telephone': '01 42 96 38 99', 'prenom': 'test', 'typeClient': '1'}
    x = client.createOrUpdateClientEx(client=bob)
    return HttpResponse("x = {}".format(x))

def createOrUpdateClientEx_test_2(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl" 
    client = SoapClient(wsdl = wsdl,
                        # cache = None,
                        ns="ges",
                        namespace= "http://www.gesmag.com"
                        soap_ns="soapenv",
                        trace= True,
                        )
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                # 'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    bob = {'ville': 'PARIS', 'societe': 'FEDERATION FRANCAISE DES', 'adresse1': 'PAPETIERS ET SPECIALISTES', 'cp': '75001', 'adresse2': '12 RUE DES PYRAMIDES', 'nom': 'test', 'telephone': '01 42 96 38 99', 'prenom': 'test', 'typeClient': '1'}
    x = client.createOrUpdateClientEx(client=bob)
    return HttpResponse("x = {}".format(x))




