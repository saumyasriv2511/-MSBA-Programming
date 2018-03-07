import requests
from pandas import DataFrame
import pandas as pd

url = 'http://www.jcpenney.com/m/jcpenney-coupons/N-mpi6e5'
r = requests.get(url)
html_content = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content)

deal_list=[]
code_list=[]
date_list=[]

offer_list = soup.find_all('li',attrs = {'class':'couponItem_new'})

for offer in offer_list:

    try:
        deal =offer.find('div', attrs={'class':'couponItem_title_new'}).text
        deal=deal.encode('utf-8').strip('\r\t\n')

    except:
        deal ='No deal'
    
    
    try:
        promo_code =offer.find('div', attrs={'class':'couponItem_code_value'}).text
        promo_code==promo_code.encode('utf-8').strip('\r\t\n')

    except:
        promo_code='No promo code'
        
    try:
        date =offer.find('div', attrs={'class':'couponItem_validity_new'}).text
        date=date.encode('utf-8').strip('\r\t\n')
        
    except:
        date ='No date'
        
    
    
    deal_list.append(deal)
    code_list.append(promo_code)
    date_list.append(date)
    
#JC = DataFrame([deal_list,code_list,date_list])
JC = DataFrame({'Deals':deal_list,'Code':code_list,'Date':date_list})
    

writer=pd.ExcelWriter('JC.xlsx')
JC.to_excel(writer,'Sheet1')
writer.save()
    