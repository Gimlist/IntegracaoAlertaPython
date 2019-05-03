#!/usr/bin/env python
# coding: utf-8

import urllib3
import requests

url = 'http://soap.alertafiscalintranet.com.br/WsSolicitacaoCadastro.asmx'

headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
 <soap:Header>
 <ValidationSoapHeader xmlns="http://soap.alertafiscalintranet.com.br">
 <Id>4500</Id>
 <Token>d2b8a6046256447396b7f0de30d8bfd5</Token>
 </ValidationSoapHeader>
 </soap:Header>
 <soap:Body>

 </soap:Body>
</soap:Envelope>"""

response = requests.post(url,data=body,headers=headers)

response

response. content

http = urllib3.PoolManager()

r = http.request('GET',url)  
r.status




