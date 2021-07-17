#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


#-*- coding: utf-8 -*-


# In[3]:


get_ipython().system('pip install requests')


# In[4]:


get_ipython().system('pip install openpyxl')


# In[15]:


get_ipython().system('pip install pandas')


# In[18]:


import pandas
from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook




HaccpInfor = {}

namelist = []
companylist=[]
businessitemnmlist=[]
productgblist=[]
imgurllist=[]
page = 1


for page in range(20):
    url = 'http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService?ServiceKey=3e%2BxITG3ESne4UwH7%2FxQ%2BNajrByAAxIpr9HmQSk5M%2Fte5wTA5OWPXLonke13WXBRhiZatSAtdfhSGu9dvnD8YA%3D%3D&numOfRows=100&pageNo='+str(page)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    productGb=soup.find_all('productgb')
    prdlstNm = soup.find_all('prdlstnm')
    businessitemNm = soup.find_all('businessitemnm')
    imgurl=soup.find_all('imgurl1')
    company = soup.find_all('company')
    for code in productGb:
        productgblist.append(code.text)
    for code in prdlstNm:
        namelist.append(code.text)
    for code in businessitemNm:
        businessitemnmlist.append(code.text)
    for code in imgurl:
        imgurllist.append(code.text)
    for code in company:
        companylist.append(code.text)

    

HaccpInfor['PrdlstNm'] = namelist
HaccpInfor['BusinessitemNm']= businessitemnmlist
HaccpInfor['ProductGb'] = productgblist
HaccpInfor['Company'] = companylist


df = pandas.DataFrame(HaccpInfor)

df.to_excel("haccpdata.xlsx",  encoding='utf-8')


# In[20]:


a=input().split()
n=input().split()

n=list(map(float, n))

d={}

for i in range(len(a)):
    d[a[i]]= n[i]

print(d)


# In[ ]:




