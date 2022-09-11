from bs4 import BeautifulSoup 
import requests


yorumlar=[]
url_1="https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf&gl=TR"




r_1 = requests.get(url_1)
soup_1=BeautifulSoup(r_1.content,"lxml")

oyun_1=soup_1.find_all("div",attrs={"class":"EGFGHd"})

for oy in oyun_1:
    
    yorumlar.append(oy.find("div",attrs={"class":"h3YV2d"}).text)
    
    
    

    