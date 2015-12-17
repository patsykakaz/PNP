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

import xml.sax

get_backends()

# base64.b64encode(hashlib.sha1("MBC2015").digest())
# >>> 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw='
# base64.b64encode(hashlib.sha1("MBC1475").digest())
# >>> 'pYsIJKF18hj0SvS3TwrQV3hWzD4='

wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl" 
client = SoapClient(wsdl = wsdl,
                    # cache = None,
                    namespace= "http://www.gesmag.com",
                    ns="ges",
                    soap_ns="soapenv",
                    trace= False,
                    )
client['wsse:Security'] = {
       'wsse:UsernameToken': {
            'wsse:Username': 'admin.webservices@mbc.com',
            'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
            # 'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
            }
        }

def test(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location = "http://dev.aboweb.com/aboweb/ClientService",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    params = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?>
        <ges:authenticateByEmail xmlns:ges="http://www.gesmag.com/">
            <email>
                patsykakaz@test.test
            </email>
            <encryptedPassword>
                tg0SG0OKOAw0PV7DwgN1ZLgv/vM=
            </encryptedPassword>
        </ges:authenticateByEmail>""");
    response = client.call("authenticateByEmail",params)
    print "***"
    print repr(response)
    print "***"

    return HttpResponse("<h1>RESPONSE</h1> <br /> <h3>{}</h3>".format(repr(response)))


def get_client(request,codeClient):
    result = client.getClient(codeClient=codeClient)
    return HttpResponse("txt = {}".format(result))

def piwi(request,username,password):
    k = authenticate(username=username,password=password)
    print "user = {}, type = {}".format(k,type(k))
    if k:
        login(request, k)
    return HttpResponse("txt = {} <br /> is_staff = {}".format(request.user, request.user.is_staff))


def aboweb(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location = "http://dev.aboweb.com/aboweb/ClientService")
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    bob = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?><ges:createOrUpdateClientEx xmlns:ges="http://www.gesmag.com/"><client><adresse1>Cuypstraat 22-III</adresse1><adresse2>1072CT</adresse2><adresse3>Amsterdam</adresse3><civilite></civilite><codeClient></codeClient><codeNii></codeNii><codeTiers></codeTiers><cp>1072CT</cp><creation></creation><email>philippe@lesidecar.fr</email><erreurAel></erreurAel><modification></modification><motPasseAbm>inyourface</motPasseAbm><nbNpai></nbNpai><nePasDiffuser></nePasDiffuser><nom>test</nom><noteEtat></noteEtat><noteNpai></noteNpai><npai></npai><origineAbm></origineAbm><pasEmailing></pasEmailing><pasMailing></pasMailing><portable></portable><prenom>test</prenom><reaboAuto></reaboAuto><relancerPaye></relancerPaye><siret></siret><societe>LSC</societe><tauxRemiseAbo></tauxRemiseAbo><telecopie></telecopie><telephone>0123456789</telephone><typeClient>0</typeClient><ville>PARIS</ville></client></ges:createOrUpdateClientEx>""");
    print "about to call createOrUpdateClientEx"
    response = client.call("createOrUpdateClientEx", bob)
    xml = SimpleXMLElement(client.xml_response)
    print xml('codeClient')
    return HttpResponse("httpreponse = {}".format(xml))


@login_required
def req(request):
    return HttpResponse('U bent ingelogged')

def kill(request):
    logout(request)
    return HttpResponse('logged out')

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




