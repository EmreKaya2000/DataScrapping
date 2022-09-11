from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
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

yorumlar=[]
browser = webdriver.Chrome("C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe",chrome_options=options)
SCROLL_PAUSE_TIME = 0.5
last_height = browser.execute_script("return document.body.scrollHeight")


browser.get("https://www.sitejabber.com/categories/wedding-dresses")
ürünler=browser.find_element(By.XPATH,'//*[@id="all-sites-section"]/div/div[3]/div[2]/div[1]')
linkler=[]
for i  in range (3,29):
 try:
     ürünler_3=ürünler.find_element(By.XPATH,'//*[@id="all-sites-section"]/div/div[3]/div[2]/div[1]/div['+str(i)+']/div[2]/a[1]')
     link=ürünler_3.get_attribute('href')
     linkler.append(link)
     browser.get(link)
     
     try:
         
         yorum=browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[5]/div[1]/div[1]/div[2]/div[1]/div['+str(i)+']/div/div[2]/div[1]/div[3]/p')
         yorumlar.append(yorum.text)
     except:
         try:
          for yo in range(2,300):
            sayfalar=ürünler.find_element(By.XPATH,'//*[@id="reviews"]/div[2]/div[2]/div[2]/span['+str(yo)+']/a')
            links=sayfalar.get_attribute("href")
            browser.get(links)
         except:
            break
         
     
 except:
     try:
      for j in range(2,500):
        sayfalar=ürünler.find_element(By.XPATH,'//*[@id="all-sites-section"]/div/div[3]/div[2]/div[2]/div[2]/span['+str(j)+']')
        links=sayfalar.get_attribute("href")
        browser.get(links)
     except:
        j