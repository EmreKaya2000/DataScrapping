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
browser = webdriver.Chrome("C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe",chrome_options=options)
browser.get("https://www.noon.com/uae-en/baby_product-bestsellers-ae/?limit=50&page=1&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")

time.sleep(3)                                                             
#a=browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/div')
#a.click()
time.sleep(1)

#b=browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/ul/li[3]')
#b.click()
time.sleep(3)  
#dildeğiştirbutonu= browser.find_element(By.XPATH,'/html/body/div[1]/div/header/div[1]/div[2]/div[3]/div[1]').click()
yorumlar=[]
for p in range(1,300):
    ürünlinkleri=[]
    for i in range(1,100):
        
            time.sleep(0.3)
            try:
                linkler=browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div[2]/div[1]/span['+str(i)+']/a')
                links=linkler.get_attribute("href")  
                ürünlinkleri.append(links)
                
            except:
                  i
                                   
        
        
       
   
    for ür in ürünlinkleri:
        browser.get(ür)
        time.sleep(0.2)
        print("yorumlar")
        try:
          
          browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div[2]/div/div/div[1]/div/button[3]').click()
          print("tıkladıı")
          
        except NameError:
            browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div[2]/div/div/div[1]/div/button[2]').click()
            print("tıkladıı")
            
        except:
            print("tıklamadı")
            break
        for but in range(0,1000):
            
           
             try:
                for y in range(1,8):

                  yorum=browser.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div['+str(y)+']/div[2]')
                  yorumlar.append(yorum.text)
             except:
                      y
             

             try:
                 
                 butons=browser.find_element(By.CLASS_NAME,'reviews-medley-footer')
                 time.sleep(2)
                 
                 butons.click()
                 print("next page")
             except:
                 print(" b")
                 break
                 but=1001
                 ""
                       
    del(ürünlinkleri)
    try:
        browser.get("https://www.noon.com/uae-en/baby_product-bestsellers-ae/?limit=50&page="+str(p+1)+"&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
        
    except:
        print("")
        break            
                
        
        








                                        
