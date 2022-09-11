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
browser.get("https://khamsat.com/training")

katagoriler=[]
yorumlar=[]
for ka in range(1,15):
    try:
        katagori=browser.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/ul/li['+str(ka)+']/a ')
        katagoriler.append(katagori.get_attribute("href"))
    except:
        ka
    try:
        katagoris=browser.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/ul/li[4]/ul/li['+str(ka)+']/a')
        katagoriler.append(katagoris.get_attribute("href"))
    except:
        ka
for kat in katagoriler:
    linkler=[]
    browser.get(kat)
    
    for i in range(0,500):
        try:
                button=browser.find_element(By.XPATH,'//*[@id="load_more_content"]').click()
        except:
            break
    
    for j in range(1,500):
     try:
         link=browser.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div[1]/div['+str(j)+']/div/div[1]/div[1]/div[1]/a')
         linkler.append(link.get_attribute("href"))
     except:
         break
    for lin in linkler:
        browser.get(lin)
        for o in  range(1,500):
            try:
                yorum=browser.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div[6]/div[2]/div/div['+str(o)+']/div/p')
                yorumlar.append(yorum.text)
            except:
                break
    del(linkler
        )