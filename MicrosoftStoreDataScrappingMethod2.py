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
browser = webdriver.Chrome("C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe",chrome_options=options)
katagoriler=["https://apps.microsoft.com/store/category/Business?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Developer%20tools?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Education?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Entertainment?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Health%20&%20fitness?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Kids%20&%20family?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Lifestyle?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Multimedia%20design?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Music?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/collections/photoandvideoediting?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/News%20&%20weather?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Personal%20Finance?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Personalization?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Security?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Shopping?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Social?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Sports?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Travel?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/category/Utilities%20&%20t?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/get-started?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/collections/BestProductivityApps?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/windows-themes?hl=ar-sa&gl=sa","https://apps.microsoft.com/store/apps?hl=ar-sa&gl=sa"]

linkbaşı="https://apps.microsoft.com"
büto=1
kato=1
bütünlinkler=[]



SCROLL_PAUSE_TIME = 1
last_height = browser.execute_script("return document.body.scrollHeight")
for kat in katagoriler:
    
    bütünlinkler=[]
    browser.get(kat)
    while True:
    # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        if last_height>60000:
            break


    for t in range(1,1000):
        try:
       
            linkler=browser.find_element(By.XPATH,'//*[@id="all-products-listall-list-container"]/div/div['+str(t)+']/div/a')
            a=linkler.get_attribute('href')
            bütünlinkler.append(a)
        
        except:
            t=t+1    
        
    for büt in bütünlinkler:
        

        browser.get(büt)
        print(kato,".katogori",büto,".uygulama")
        büto=büto+1
        for i in range(0,1000):
            try:
                
                j=browser.find_element(By.XPATH,'//*[@id="LoadMoreReviews"]').click() 
                time.sleep(0.5)
    
    
    
            except:
                    i
        
                
        if len(yorumlar)>37000:
            break
        for o in range(1,1000):
                try:
                    
                    yorumlars=browser.find_element(By.XPATH,'//*[@id="review-list"]/div['+str(o)+']/div/p')
                    yorumlar.append(yorumlars.text)
             
                except:
                    break     
    kato=kato+1       
    del(bütünlinkler)   

    
    


    
   
   
 