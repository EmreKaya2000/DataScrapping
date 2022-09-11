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
url_0="https://apps.microsoft.com/store/category/Business"
linkbaşı="https://apps.microsoft.com"
browser.get(url_0)
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

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
    if last_height>30000:
        break


for t in range(1,1000):
    try:
       
        linkler=browser.find_element(By.XPATH,'//*[@id="all-products-listall-list-container"]/div/div['+str(t)+']/div/a')
        a=linkler.get_attribute('href')
        print(a)
        browser.get(a)
        print(t,".link==",a)
        for i in range(0,1000):
            try:
                
                j=browser.find_element(By.XPATH,'//*[@id="LoadMoreReviews"]').click()    
    
    
    
            except:
                j=browser.find_element(By.XPATH,'//*[@id="LoadMoreReviews"]').click()
        
                
            
        for o in range(1,1000):
            try:
                    
             yorumlars=browser.find_element(By.XPATH,'//*[@id="review-list"]/div['+str(o)+']/div/p')
             yorumlar.append(yorumlars.text)
             browser.execute_script("window.history.go(-1)")
            except:
               break
    except:
        t=t+1
    


    
   
    
 