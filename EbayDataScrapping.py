from bs4 import BeautifulSoup ,NavigableString, Tag
import requests
import pandas as pd
yıldızlar=[]
başlıklar=[]
yorumlar=[]
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
url_0="https://www.ebay.com/b/iPhone-11/9355/bn_7116334163"
r_0 = requests.get(url_0,headers=header)
soup_0=BeautifulSoup(r_0.content,"lxml")
ürünler=soup_0.find_all("ul",attrs={"class":"b-list__items_nofooter srp-results srp-grid"})
for ür in ürünler:
    
 linkler=ür.find_all("li",attrs={"class":"s-item s-item--large"})
 for i in range(0,len(linkler)):
  asıllink=(linkler[i].a.get("href"))
  url =asıllink
  r= requests.get(url)
  soup=BeautifulSoup(r.content,"lxml")
  ürün=soup.find("div",attrs={"class":"reviews"})
  if ürün is None :
         continue
     
  bütünyorumlar=ürün.find_all("div",attrs={"class":"ebay-review-section"})
  for i in range (0,len(bütünyorumlar)):
     yorum=bütünyorumlar[i].find("div",attrs={"class":"ebay-review-section-r"})
     yıldız=bütünyorumlar[i].find("div",attrs={"class":"ebay-review-section-l"})
     yıldızsay=yıldız.find("span",attrs={"class":"star-rating"})
     yıldızsayısı=yıldızsay.find_all("i",attrs={"class":"fullStar"})
     
     if len(yorum)<3:
           continue
     başlıklar.append(yorum.find("p",attrs={"itemprop":"name"}).text)
     yıldızlar.append(len(yıldızsayısı))
     yorumlar.append(yorum.find("p",attrs={"itemprop":"reviewBody"}).text)
       

