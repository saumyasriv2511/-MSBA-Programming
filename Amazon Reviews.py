from bs4 import BeautifulSoup
import requests

def text_with_newlines(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += '\n'
    return text

#url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=1"
# url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=2"
# url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_getr_d_paging_btm_3?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=3"
# url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=4"
# url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_getr_d_paging_btm_4425?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=4425
# url = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=1
#https://www.amazon.com/Estee-Lauder-Advanced-Synchronized-Recovery/product-reviews/B00E26SFKK/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=2
#https://www.amazon.com/Estee-Lauder-Advanced-Synchronized-Recovery/product-reviews/B00E26SFKK/ref=cm_cr_getr_d_paging_btm_3?ie=UTF8&reviewerType=avp_only_reviews&pageNumber=3

txt = open('EsteeLauderreviews.txt', 'w')


ur1='https://www.amazon.com/Estee-Lauder-Advanced-Synchronized-Recovery/product-reviews/B00E26SFKK/ref=cm_cr_arp_d_paging_btm_'
ur2='?ie=UTF8&reviewerType=avp_only_reviews&pageNumber'
for i in range(1,5):
    page=ur1+str(i)+ur2+str(i)
    items=''
    # add header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    r = requests.get(page, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    reviews =soup.find('div',attrs={'class':'a-row review-data'})
    for tag in soup.find_all('div',attrs={'class':'a-row review-data'}):
        new=text_with_newlines(tag.contents[0])
        items+=new.encode('utf-8')
    txt.write(items)

txt.close()