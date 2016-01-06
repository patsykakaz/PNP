

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
    # params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><codeClient>'+codeClient+'</codeClient></ges:getClient>');
    # result = client.call("getClient",params)
    # xml = SimpleXMLElement(client.xml_response)
    # print repr(xml)
    print "---------°°°°°°°°----------"
    # target = xml.children().children().children()
    # target.password = 'MBCTEST2'
    target = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?><ges:createOrUpdateClientEx xmlns:ges="http://www.gesmag.com/"><client><adresse1>Cuypstraat 22-III</adresse1><adresse2>1072CT</adresse2><adresse3>Amsterdam</adresse3><civilite></civilite><codeClient>8741</codeClient><codeNii></codeNii><codeTiers></codeTiers><cp>75011</cp><creation></creation><email>shark@shark.shark</email><erreurAel></erreurAel><modification></modification><motPasseAbm>aboweb</motPasseAbm><nbNpai></nbNpai><nePasDiffuser></nePasDiffuser><nom>test</nom><noteEtat></noteEtat><noteNpai></noteNpai><npai></npai><origineAbm></origineAbm><pasEmailing></pasEmailing><pasMailing></pasMailing><portable></portable><prenom>test</prenom><reaboAuto></reaboAuto><relancerPaye></relancerPaye><siret></siret><societe>LSC2</societe><tauxRemiseAbo></tauxRemiseAbo><telecopie></telecopie><telephone>0123456789</telephone><typeClient>0</typeClient><ville>PARIS</ville></client></ges:createOrUpdateClientEx>""")

    client.call('createOrUpdateClientEx',target)
    return HttpResponse('ok')


def testCoUCX(request):
    codeClient = '8741'
    client = SoapClient(location="http://aboweb.com/aboweb/ClientService?wsdl",trace=True)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><codeClient>'+codeClient+'</codeClient></ges:getClient>');
    result = client.call("getClient",params)
    xml = SimpleXMLElement(client.xml_response)
    print repr(xml)
    print "---------°°°°°°°°----------"
    target = xml.children().children().children()
    target.password = 'MBCTEST2'
    target = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><client><adresse1/><adresse2>16 RUE ST FIACRE</adresse2><adresse3/><civilite>M</civilite><codeClient>8741</codeClient><cp>75002</cp><email>pnp@groupembc.com</email><motPasseAbm>MBCTEST1</motPasseAbm><nePasDiffuser>false</nePasDiffuser><nom>LEROI</nom><origineAbm/><pasEmailing>false</pasEmailing><pasMailing>false</pasMailing><portable/><prenom>XXXXXXX</prenom><reaboAuto>false</reaboAuto><relancerPaye>false</relancerPaye><societe>MBC</societe><tauxRemiseAbo>0.0</tauxRemiseAbo><telecopie/><telephone/><typeClient>0</typeClient><ville>PARIS</ville></client></ges:getClient>')
    print type(target)

    client.call('createOrUpdateClientEx',target)
    return HttpResponse('ok')

