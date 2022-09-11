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
browser.get("https://www.etsy.com/listing/105238562/wedding-dress-bridal-shower-gift-gift?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-1&pro=1&sts=1")
time.sleep(2)
button = browser.find_element(By.XPATH,'/html/body/main/div[1]/div[1]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/button[2]')
button.click()
yorumlar=[]


for say in range (0,8000):
    for i in range(1,6):
        try:
            yorum=browser.find_element(By.XPATH,'/html/body/main/div[1]/div[1]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div['+str(i)+']/div/div/div[1]/div[2]/div/div/div/p')
        
            textyorum=yorum.text
            yorumlar.append(textyorum)
            
            
        except:
            i
    time.sleep(0.75)                                                                                                                                                       
    if say < 2 :
        
        try:
            
            diğerbutton =browser.find_element(By.XPATH,'/html/body/main/div[1]/div[1]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div[2]/nav/ul/li[6]/a/span[2]')
            diğerbutton.click()
        except:
                say
    else :
        try:
            
            diğerbutton =browser.find_element(By.XPATH,'/html/body/main/div[1]/div[1]/div/div/div[1]/div[4]/div/div/div[2]/div/div/div[2]/nav/ul/li[7]/a/span[2]')
            diğerbutton.click()
        except:
                say