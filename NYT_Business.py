import urllib2
from bs4 import BeautifulSoup
import requests

txt = open('bstest3.txt', 'w')
soup = BeautifulSoup(urllib2.urlopen('http://www.nytimes.com/pages/business/index.html').read())
x=[]
for a in soup.find_all('h2'):
    for b in a.find_all('a',href=True):
        if "2017" in b['href']:
             x.append(b['href'])
session = requests.Session()  
for u in x:                             
    url = u
    req = session.get(url)
    soup = BeautifulSoup(req.text)

    # the article title 
    try:
        if soup.find('title'):
            title=soup.find('title')
        else:
            title=soup.find('h1')
        txt.write('\n'+ '\n' + "Title: " + str(title.string) + '\n')
            
        #title = soup.find("h1")
        #txt.write('\n'+ '\n' + "Title: " + str(title.string) + '\n')
    except:
        txt.write('\n'+ '\n'+ "Title: cannot find the title "+ '\n' )
        txt.write( '\n'+ '\n'+str(u)+ '\n')
            
    # the article date
    try:
        date = soup.find("time", {'class':'dateline'}).text
        txt.write('\n'+"Date: " + str(date) + '\n')
    except:
        txt.write('\n'+'Date: Could not find the title' + '\n')
        txt.write( '\n'+ '\n'+str(u)+ '\n')
        
    # the article author     
    try:
        byline=soup.find("span", {'class':'byline-author'}).text
        txt.write('\n'+"Author: " + str(byline) + '\n')
    except:
        txt.write('\n'+"Could not find the author!"+ '\n')
        txt.write( '\n'+ '\n'+str(u)+ '\n')
    
    # the article contents     
    p_tags = soup.find_all(class_="story-body-text story-content")
    article2 = ''.join(p_tag.get_text() for p_tag in p_tags)
    article1 = article2.encode('utf-8')
    for row in article1:
        txt.write(row)
    
    
txt.close()