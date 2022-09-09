from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
"""
Proflii belirtme
"""
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\emre_\AppData\Local\Google\Chrome Beta\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#yıldızlar=[]
yorumlar=[]
url_0="https://play.google.com/store/games"
linkbasi="https://play.google.com"
Linkbasi_2="https://play.google.com/"


def document_initialised(driver):
    return driver.execute_script("return initialised")

"""
Ana Sayfa Kazıma
"""
r_0 = requests.get(url_0)
browser = webdriver.Chrome("C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe",chrome_options=options)
soup_0=BeautifulSoup(r_0.content,"lxml")
linkler=soup_0.find_all("a",attrs={"class":"uEz1ib"})

for i in range(4,len(linkler)): # katagoriler döngüsü
    link_0=linkler[i].get("href")
    url_1=linkbasi+link_0
    print(url_1)
    browser.get(url_1)
    

    r_1 = requests.get(url_1)
    soup_1=BeautifulSoup(r_1.content,"lxml")
    cihazlar=soup_1.find("div",attrs={"class":"bewvKb DUDfsf"})
    cihazlar_2=cihazlar.find("div",attrs={"class":"aoJE7e rE4BKe"})
    xler=cihazlar_2.find_all("div",attrs={"class":"ULeU3b"})
    

    if i !=3:
        for j in xler: #Cihazlar döngüsü
            link_2=j.a.get("href")
            cihazlaarın_urlsi=Linkbasi_2+link_2
            print(cihazlaarın_urlsi)
            r_2 = requests.get(cihazlaarın_urlsi)
            soup_2=BeautifulSoup(r_2.content,"lxml")
            oyunlar=soup_2.find_all("div",attrs={"class":"ULeU3b neq64b"}) 
            
            for oy in range (5,len(oyunlar)):
                len(yorumlar)
                oyun=oyunlar[oy].find("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc"})
                print(i,".link ",oy-3,". oyun")
                try:
                    link=oyun.a.get("href")
                    url_0=linkbasi+link
                    
            
            
                    browser.get(url_0)
                   
                    
                    try:
                     print("yanlış yer")
                     if (i==2):
                             
                                   
                             l=browser.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[3]/section/div/div/div[5]/div/div/button').click()
                             
                             yorumlars=browser.find_elements(By.CLASS_NAME,"h3YV2d")
                             
                    
                 
                     else:
                         print("yanlışyer")
                         try:
                            
                             l=browser.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[4]/section/div/div/div[5]/div/div/button').click()
                             yorumlars=browser.find_elements(By.CLASS_NAME,"h3YV2d")  
                         except:
                              browser.refresh()
                     for yo in yorumlars:
                         yorumlar.append(yo.text)
                    except:
                        oy=oy+1
                
                except:
                        oy=oy+1
    
    else:               
         
          oyunlar=soup_1.find_all("div",attrs={"class":"ULeU3b neq64b"}) 
          for oy in range (3,len(oyunlar)):
              len(yorumlar)
              oyun=oyunlar[oy].find("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc"})
              print(i,".link ",oy-2,". oyun")
            
              try:
                  
                  link=oyun.a.get("href")
                  url_0=linkbasi+link
          
                 
          
                  browser.get(url_0)
                  
                  
                  try: 
                      print("Deneme 11111111")
                      l=browser.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[3]/section/div/div/div[3]/div/div/button').click()
                      yorumlars=browser.find_elements(By.CLASS_NAME,"h3YV2d")
                      for yo in yorumlars:
                          yorumlar.append(yo.text)
                  except NoSuchElementException:
                        print("Deneme 22222222")
                        l=browser.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[3]/section/div/div/div[4]/div/div/button').click()
                        yorumlars=browser.find_elements(By.CLASS_NAME,"h3YV2d")
                        for yo in yorumlars:
                            yorumlar.append(yo.text)    
                  else:
                        print("Deneme 33333333")
                        l=browser.find_element(By.XPATH,'/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[3]/section/div/div/div[5]/div/div/button').click()
                        yorumlars=browser.find_elements(By.CLASS_NAME,"h3YV2d")
                        for yo in yorumlars:
                            yorumlar.append(yo.text)
                  
                      
                      
                  
              except:
                      oy=oy+1  

