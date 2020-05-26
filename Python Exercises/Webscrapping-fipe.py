import time 
import threading
import string
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import requests
import re
import numpy as np

# 1 - Catch HTML content through URL
url = "https://veiculos.fipe.org.br/#carro"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(2)
element = driver.find_element_by_xpath(
    "//*[(@id = 'selectMarcacarro')]")
html_content=element.get_attribute('outerHTML')
#Catch vehicle's brand
value=[]
brand=[]
only_option_tags=SoupStrainer("option")
soup1=BeautifulSoup(html_content,'html.parser',parse_only=only_option_tags)
print(soup1.prettify())
for marcas in soup1.find_all("option"):
    value.append(marcas['value'])
    brand.append(marcas.get_text())
df = pd.DataFrame({'Indice': value, 'Modelo': brand})
df=df.drop(0)
qtdyvehicles=df.shape[0]
print(df)
print(qtdyvehicles)


element = driver.find_element_by_xpath(
    "//*[(@id = 'selectMarcacarro')]")
html_content=element.get_attribute('outerHTML')
print(html_content)
    


driver.quit()
