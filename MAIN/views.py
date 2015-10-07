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


# >>> base64.b64encode(hashlib.sha1("MBC2015").digest())
# 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw='
# >>> base64.b64encode(hashlib.sha1("MBC1475").digest())
# 'pYsIJKF18hj0SvS3TwrQV3hWzD4='

wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl" 
client = SoapClient(wsdl = wsdl,
                    cache = None,
                    ns="ges",
                    soap_ns="soapenv",
                    trace=False
                    )
client['wsse:Security'] = {
       'wsse:UsernameToken': {
            'wsse:Username': 'admin.webservices@mbc.com',
            'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
            }
        }

def test(request):

    result = client.getClients(132000)
    print result
    # k = authenticate(username='test@test.test', password='test')
    # login(request, k)
    return HttpResponse("<h1>CLIENTS</h1> <br />{}".format(result))

def get_client(request):

    client = SoapClient(wsdl="http://dev.aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=True)
    client['AuthHeaderElement'] = {'Login': 'admin.webservices@mbc.com', 'Password': 'mbc2015'}
    txt = client.ABM_ACCES_BASE(600,12,17)
    return HttpResponse(txt)

def aboweb(request):
    bob = client.getClient(codeClient=654)
    bob = bob['client']
    print "user to work -> {}".format(bob)
    # bob = {'ville': 'PARIS', 'societe': 'FEDERATION FRANCAISE DES', 'adresse1': 'PAPETIERS ET SPECIALISTES', 'cp': '75001', 'adresse2': '12 RUE DES PYRAMIDES', 'nom': 'test', 'telephone': '01 42 96 38 99', 'prenom': 'test', 'typeClient': '1'}
    # bob['tauxRemiseAbo'] = double(bob['tauxRemiseAbo'])
    print "**"
    print bob['typeClient']
    print type(bob['typeClient'])
    print "**"
    bob['typeClient'] = bob['typeClient'].encode('utf8')
    x = client.createOrUpdateClientEx(client=bob)
    # x = client.getClient(codeClient=655)
    # for k,v in x['client'].items():
    #     print("** {} = {} -({})** ".format(k,v,type(v)))
    return HttpResponse("x = {}".format(x))


@login_required
def req(request):
    return HttpResponse('U bent ingelogged')

def kill(request):
    logout(request)
    return HttpResponse('logged out')

def archive(request,start,end):
    from mezzanine.blog.models import BlogPost
    from db_PNP import DB
    
    start,end = int(start), int(end)

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
            k = BlogPost(user_id=1,
                        title=item[2].decode('utf-8'),
                        content=content,
                        featured_image=u,
                        publish_date=item[8],
                        archive=True
                        )
        else: 
            k = BlogPost(user_id=1,
                        title=item[2].decode('utf-8'),
                        content=content,
                        featured_image=u,
                        publish_date=item[15],
                        archive=True
                        )
            print item[15]
        k.save()
    # txt = txt.decode('utf-8')

    return HttpResponse(k.title)

