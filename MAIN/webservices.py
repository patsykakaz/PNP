#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from base64 import b64encode
from hashlib import sha1
# 
from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *

def aboAuth(username,password):
    # wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location = "http://aboweb.com/aboweb/ClientService",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:authenticateByEmail xmlns:ges="http://www.gesmag.com/"><email>'+username+'</email><encryptedPassword>'+ b64encode(sha1(password).digest()) +'</encryptedPassword></ges:authenticateByEmail>')
    response = client.call("authenticateByEmail",params)
    xml = SimpleXMLElement(client.xml_response)
    return str(xml('result'))

def ABM_ACCES_CLIENT(username,password):
    clientABM = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=False)
    clientABM['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    resultABM = clientABM.ABM_ACCES_CLIENT('207',username,password)
    xml = SimpleXMLElement(clientABM.xml_response)
    return xml('codeClient')

def getAbonnements(codeClient):

    clientAbonnement = SoapClient(location ="http://aboweb.com/aboweb/AbonnementService",trace=False)
    clientAbonnement['wsse:Security'] = {
                    'wsse:UsernameToken': {
                        'wsse:Username': 'admin.webservices@mbc.com',
                        # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                        'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                    }
                }

    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getAbonnements xmlns:ges="http://www.gesmag.com/"><codeClient>%s</codeClient><offset>0</offset></ges:getAbonnements>' % codeClient)
    result = clientAbonnement.call("getAbonnements",params)
    xml = SimpleXMLElement(clientAbonnement.xml_response)
    return xml