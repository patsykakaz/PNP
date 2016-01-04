#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.utils.http import base36_to_int
from django.core.mail import send_mail

from .models import Client
User = get_user_model()

from base64 import b64encode
from hashlib import sha1
import uuid
from django.contrib.auth.hashers import make_password

from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *

# wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
client = SoapClient(location = "http://aboweb.com/aboweb/ClientService",trace=False)
client['wsse:Security'] = {
       'wsse:UsernameToken': {
            'wsse:Username': 'admin.webservices@mbc.com',
            # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
            }
        }

clientAbonnement = SoapClient(location ="http://aboweb.com/aboweb/AbonnementService",trace=False)
clientAbonnement['wsse:Security'] = {
                'wsse:UsernameToken': {
                    'wsse:Username': 'admin.webservices@mbc.com',
                    # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                    'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }

clientABM = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=False)
clientABM['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}

class ClientAuthBackend(ModelBackend):

    def authenticate(self, **kwargs):
        print "*** auth 2.0 starting ***"
        if kwargs:
            username = kwargs.pop("username", None)
            if username:
                username_or_email = (Q(username=username) | Q(email=username)) & Q(is_staff=True)
                password = kwargs.pop("password", None)
                try:
                    user = User.objects.get(username_or_email, **kwargs)
                except User.DoesNotExist:
                    print "Checking aboWeb for Auth"
                    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:authenticateByEmail xmlns:ges="http://www.gesmag.com/"><email>'+username+'</email><encryptedPassword>'+ b64encode(sha1(password).digest()) +'</encryptedPassword></ges:authenticateByEmail>');
                    response = client.call("authenticateByEmail",params)
                    xml = SimpleXMLElement(client.xml_response)
                    if str(xml('result')) == 'true':
                        print 'user authenticated in aboweb'
                        # user exists in aboWeb. Fetch codeClient with low security SOAP access
                        resultABM = clientABM.ABM_ACCES_CLIENT('207',username,password)
                        xml = SimpleXMLElement(clientABM.xml_response)
                        codeClient = xml('codeClient')

                        # fetch "getAbonnements"
                        params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getAbonnements xmlns:ges="http://www.gesmag.com/"><codeClient>%s</codeClient><offset>0</offset></ges:getAbonnements>' % codeClient)
                        result = clientAbonnement.call("getAbonnements",params)
                        xml = SimpleXMLElement(clientAbonnement.xml_response)
                        for abonnement in xml.children().children().children():
                            if int(abonnement.refTitre) == 26 and str(abonnement.obsolete) == 'false':
                                print "active_abo Found"
                                active_abo = True

                        # Green light from aboWeb
                        if active_abo:
                            username_or_email = Q(username=username) | Q(email=username)
                            try:
                                user = User.objects.get(username_or_email, **kwargs)
                                if user.check_password(password):
                                    print "user is being auth. through local db"
                                    return user
                            except User.DoesNotExist:
                                # add unknown user to local db
                                print "creating local user"
                                userId = str(uuid.uuid4())
                                try:
                                    # send_mail('Creation de compte', 'Message test de creation du code de l\'utilisateur : {}'.format(uuid), 'n.burton@groupembc.com', ['philippe@lesidecar.fr',],fail_silently=False)
                                   send_mail('user created', 'n.burton@groupembc.com', ['philippe@lesidecar.fr',], fail_silently=False)
                                   # send_mail('Subject here', 'Here is the message.', 'n.burton@groupembc.com', ['philippe.dagognet@gmail.com'], fail_silently=False)
                                   print "MAIL HAS BEEN SENT !"
                                except 'SMTPConnectError' as e:
                                    return HttpResponse(e)
                                k = User(username=userId,email=username,password=make_password(password),is_staff=False)
                                k.save()
                                return k

                        # RED FLAG
                        else: 
                            pass
                        
                
                    else:
                        pass
                else:
                    if user.check_password(password):
                        return user
            else:
                if 'uidb36' not in kwargs:
                    return
                kwargs["id"] = base36_to_int(kwargs.pop("uidb36"))
                token = kwargs.pop("token")
                try:
                    user = User.objects.get(**kwargs)
                except User.DoesNotExist:
                    pass
                else:
                    if default_token_generator.check_token(user, token):
                        return user