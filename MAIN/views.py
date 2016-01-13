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

def testCoUCX(request):
    codeClient = '8741'
    client = SoapClient(location="http://aboweb.com/aboweb/ClientService?wsdl",trace=True)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><codeClient>'+codeClient+'</codeClient></ges:getClient>');
    result = client.call("getClient",params)
    xml = SimpleXMLElement(client.xml_response)
    print "---------°°°°°°°°----------"
    target = xml.children().children().children()
    target.nom = 'LEROI'
    target.email = "pnp@groupembc.com"
    target.motPasseAbm = "MBCTEST1"
    target = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:createOrUpdateClientEx xmlns:ges="http://www.gesmag.com/">'+ repr(target) +'</ges:createOrUpdateClientEx>')

    client.call('createOrUpdateClientEx',target)
    return HttpResponse('ok')

def test(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location="http://dev.aboweb.com/aboweb/ClientService",trace=False)
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
    client = SoapClient(location="http://aboweb.com/aboweb/ClientService?wsdl",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><codeClient>'+codeClient+'</codeClient></ges:getClient>');
    result = client.call("getClient",params)

    xml = SimpleXMLElement(client.xml_response)
    response = repr(xml('client'))
    # response_bis = response('codeClient')
    # print"*****" + repr(response_bis) + "*****"

    print "*****" + repr(xml('client')) + "*****"
    return HttpResponse("txt = {}".format(response))

# TEST 1
def test_AbmWeb(request):
    client = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=True)
    client['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    # result = client.ABM_ACCES_BASE(600,99,99)
    result = client.ABM_ACCES_CLIENT('207','17780','27380')
    # result = client.ABM_TEST_MAIL('207','1','christiane95630@orange.fr')
    xml = SimpleXMLElement(client.xml_response)
    response = repr(xml('codeClient'))
    return HttpResponse(response)

# TEST 2
def test_ClientService(request):
    return HttpResponse('TEST2')

# TEST 3
def test_AbonnementService(request):
    # wsdl = "http://aboweb.com/aboweb/AbonnementService?wsdl" 
    client = SoapClient(location ="http://aboweb.com/aboweb/AbonnementService",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    params = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?>
        <ges:getAbonnements xmlns:ges="http://www.gesmag.com/">
            <codeClient>157095</codeClient>
            <offset>0</offset>
        </ges:getAbonnements>""")
    result = client.call("getAbonnements",params)
    print "******* REPR(RESPONSE) -> {} *******".format(repr(result))
    return HttpResponse("txt = {}".format(result))

def getAbonnement(request):
    # wsdl = "http://aboweb.com/aboweb/AbonnementService?wsdl" 
    client = SoapClient(location ="http://aboweb.com/aboweb/AbonnementService",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    params = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?>
        <ges:getAbonnement xmlns:ges="http://www.gesmag.com/">
            <refAbonnement>94982</refAbonnement>
        </ges:getAbonnement>""");
    result = client.call("getAbonnement",params)
    print "******* REPR(RESPONSE) -> {} *******".format(repr(result))
    return HttpResponse("txt = {}".format(result))


def ABMabo(request):
    client = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=True)
    client['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    result = client.ABM_LISTE_ABOS_CLIENT(207,1136)
    xml = SimpleXMLElement(client.xml_response)
    response = xml('ns2:ABM_LISTE_ABOS_CLIENTResponse')
    http = ''
    for element in response('nomEnClair'):
        print "abo += {}".format(element)
        http += "+ {}".format(element)
    return HttpResponse(http)


def aboweb(request):
    wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location = "http://dev.aboweb.com/aboweb/ClientService")
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    bob = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?><ges:createOrUpdateClientEx xmlns:ges="http://www.gesmag.com/"><client><adresse1>Cuypstraat 22-III</adresse1><adresse2>1072CT</adresse2><adresse3>Amsterdam</adresse3><civilite></civilite><codeClient>125153</codeClient><codeNii></codeNii><codeTiers></codeTiers><cp>75011</cp><creation></creation><email>shark@shark.shark</email><erreurAel></erreurAel><modification></modification><motPasseAbm>aboweb</motPasseAbm><nbNpai></nbNpai><nePasDiffuser></nePasDiffuser><nom>test</nom><noteEtat></noteEtat><noteNpai></noteNpai><npai></npai><origineAbm></origineAbm><pasEmailing></pasEmailing><pasMailing></pasMailing><portable></portable><prenom>test</prenom><reaboAuto></reaboAuto><relancerPaye></relancerPaye><siret></siret><societe>LSC2</societe><tauxRemiseAbo></tauxRemiseAbo><telecopie></telecopie><telephone>0123456789</telephone><typeClient>0</typeClient><ville>PARIS</ville></client></ges:createOrUpdateClientEx>""");
    print "about to call createOrUpdateClientEx"
    response = client.call("createOrUpdateClientEx", bob)
    xml = SimpleXMLElement(client.xml_response)
    print xml('codeClient')
    return HttpResponse("httpreponse = {}".format(xml))

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





