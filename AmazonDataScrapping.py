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

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\emre_\AppData\Local\Google\Chrome Beta\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#yıldızlar=[]
yorumlar=[]
browser = webdriver.Chrome("C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe",chrome_options=options)
linkler=[]
url_0="https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A281407&ref=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2"
browser.maximize_window()

ürünlinkler=[]
ürünlinklerdüzenli=[]
    
browser.get(url_0)
for i in range(2,100):
    try:
     
      ürünlinkleri=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div['+str(i)+']/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
      a=ürünlinkleri.get_attribute("href")      
      ürünlinkler.append(a)
                                          
    except:
            i   
    try:
        ürün=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div['+str(i)+']/div/div/div/div/div[2]/span/a')
        b=ürün.get_attribute("href")        
        ürünlinkler.append(b)
        
    except:
        i
    try:
     
      ürünlinki=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div['+str(i)+']/div/div/div/div/div/div/div[1]/span/a')
      c=ürünlinki.get_attribute("href")      
      ürünlinkler.append(c)
                                          
    except:  
        i
for ürü in ürünlinkler:
    if ürü not in ürünlinklerdüzenli:
        ürünlinklerdüzenli.append(ürü)
     

for ür in ürünlinklerdüzenli:
    try:
        
     
     browser.get(ür)
     dsa=browser.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[3]/div[101]/div/div/div[2]/div/div[2]/span[2]/div/div/div[5]/div[2]/a') #tüm yorumları görün yeri 
                                           
     j=dsa.get_attribute("href") #tüm yorumlaro gör linki 
     print("çalııyor")
     browser.get(j)#tüm yormları göre git
     
     
                        
    except:
        print(ür,"1")
    try:
        
     
     browser.get(ür)
     dsa=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[10]/div[29]/div/div/div/div[2]/div/div[2]/span[2]/div/div/div[5]/div[2]/a') #tüm yorumları görün yeri 
                                      
     j=dsa.get_attribute("href") #tüm yorumlaro gör linki 
     print("çalııyor")
     browser.get(j)#tüm yormları göre git
     
     
                        
    except:
        print(ür,"2")
    try:
        
     
     browser.get(ür)
     dsa=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[9]/div[29]/div/div/div[2]/div/div[2]/span[3]/span/div[2]/div/div/div[6]/a') #tüm yorumları görün yeri 
                                       
     j=dsa.get_attribute("href") #tüm yorumlaro gör linki 
     print("çalııyor")
     browser.get(j)#tüm yormları göre git
     
     
                        
    except:
        print(ür,"3")
    try:
       
    
     browser.get(ür)
     dsa=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[9]/div[29]/div/div/div[2]/div/div[2]/span[3]/span/div[2]/div/div/div[6]/a') #tüm yorumları görün yeri 
                                     
     j=dsa.get_attribute("href") #tüm yorumlaro gör linki 
     print("çalııyor")
     browser.get(j)#tüm yormları göre git
    
    
                       
    except:
       print(ür,"4")
    
    
    for ne in range(0,100):
        
            time.sleep(1)
            for x in range(2,50):
                try:
                    a=browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div['+str(x)+']/div/div/div[4]/span/span').text
                    yorumlar.append(a)                               
                    print("yorumlar")
                except:
                    break
                
            
            try:    
                digersayfa=browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div[12]/span/div/ul/li[2]/a')
                time.sleep(1)
                digersayfa.click()
                print("diğersayfa")
            except:
               break
        
                
            
    
    
    


 

        