from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.utils.http import base36_to_int
from django.core.mail import send_mail


from mezzanine.conf import settings

from .models import Client
User = get_user_model()

from base64 import b64encode
from hashlib import sha1
import uuid
from django.contrib.auth.hashers import make_password

from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *
wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
client = SoapClient(location = "http://dev.aboweb.com/aboweb/ClientService",trace=False)
client['wsse:Security'] = {
       'wsse:UsernameToken': {
            'wsse:Username': 'admin.webservices@mbc.com',
            'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
            }
        }



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
                    print "second round auth"
                    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:authenticateByEmail xmlns:ges="http://www.gesmag.com/"><email>'+username+'</email><encryptedPassword>'+ b64encode(sha1(password).digest()) +'</encryptedPassword></ges:authenticateByEmail>');
                    response = client.call("authenticateByEmail",params)
                    xml = SimpleXMLElement(client.xml_response)
                    if str(xml('result')) == 'true':
                        print "aboWeb grants auth"
                        username_or_email = Q(username=username) | Q(email=username)
                        try:
                            user = User.objects.get(username_or_email, **kwargs)
                            if user.check_password(password):
                                print "user is being auth. through local db"
                                return user
                        except User.DoesNotExist:
                            # CREATE LOCAL USER
                            print "creating local user"
                            userId = str(uuid.uuid4())
                            # send_mail('Creation de compte', 'Message test de creation du code de l\'utilisateur : {}'.format(uuid), 'n.burton@groupembc.com', ['philippe@lesidecar.fr','nelson@lesidecar.fr'],fail_silently=False)
                            try:
                               send_mail('testmail', 'test content', settings.EMAIL_HOST_USER, ['philippe@lesidecar.fr'], fail_silently=False)
                               # send_mail('Subject here', 'Here is the message.', 'n.burton@groupembc.com', ['philippe.dagognet@gmail.com'], fail_silently=False)
                               print "MAIL HAS BEEN SENT !"
                            except 'SMTPConnectError' as e:
                                return HttpResponse(e)
                            k = User(username=userId,email=username,password=make_password(password),is_staff=False)
                            k.save()
                            return k
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