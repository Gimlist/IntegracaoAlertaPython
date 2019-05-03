#!/usr/bin/env python
# coding: utf-8

# In[83]:


import urllib3
import requests


# In[84]:


url = 'http://soap.alertafiscalintranet.com.br/WsSolicitacaoCadastro.asmx'


# In[85]:


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


# In[86]:


response = requests.post(url,data=body,headers=headers)


# In[87]:


response


# In[88]:


response. content


# In[89]:


http = urllib3.PoolManager()


# In[90]:


r = http.request('GET',url)  
r.status


# In[ ]:





# In[ ]:





# In[ ]:




