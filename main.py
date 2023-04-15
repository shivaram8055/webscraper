from bs4 import BeautifulSoup as bs
import requests
import pandas

print('''
    WELCOME TO WEB SCRAPER..
    THIS WEB SCRAPER CAN ONLY ACCQUIRE DATA FROM FILPKART.
    IT WAS DESIGNED FOR MOBILE DATA.
    SO MAKE SURE YOU GIVE THE LINKS OF FROM FLIPKART
''')
url=input('url= ')
r=requests.get(url)
soup=bs(r.content,'html.parser')

ti=soup.findAll('div',class_='_4rR01T')
ra=soup.findAll('div',class_='_3LWZlK')
pr=soup.findAll('div',class_='_30jeq3 _1_WHN1')
rev=soup.findAll('span',class_='_2_R_DZ')
print(ti)
title=[]
rating=[]
review=[]
price=[]
for t,r,p,re in zip(ti,ra,pr,rev):
    title.append(t.text)
    rating.append(r.text)
    price.append(p.text)
    review.append(re.text)
data={'title':title,'rating':rating,'price':price,'review':review}
py=pandas.DataFrame(data=data)
py.to_csv(input('enter file name: ')+'.csv')



