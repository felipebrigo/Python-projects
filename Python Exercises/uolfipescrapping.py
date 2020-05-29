import time 
import threading
import string
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import requests
import numpy as np

# 1 - Catch HTML content through URL
url = "https://www.uol.com.br/carros/tabela-fipe"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
element=driver.find_element_by_xpath("//div[@class ='fipe-table-page']")
html_content=element.get_attribute('outerHTML')
print(BeautifulSoup(html_content,'html.parser').prettify())

select = Select(driver.find_element_by_class_name("target"))
select.select_by_visible_text("Vender")
time.sleep(3)

only_option_tags=SoupStrainer("option")
soup1=BeautifulSoup(html_content,'html.parser',parse_only=only_option_tags)
print(soup1.prettify())

"""vender=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id ='ads-interesse')]")))
vender.click()
time.sleep(2)
#select = Select(brandelements)
#select.select_by_visible_text('Troller')

element = driver.find_element_by_xpath(
    "//*[(@id = 'selectMarcacarro')]")
html_content=element.get_attribute('outerHTML')

#Catch vehicle's brand
value=[]
brand=[]

#Parse and append all data into a Dataframe
for marcas in soup1.find_all("option"):
    value.append(marcas['value'])
    brand.append(marcas.get_text())
df = pd.DataFrame({'Indice': value, 'Modelo': brand})
df=df.drop(0)
qtdyvehicles=df.shape[0]
print(df)
print(qtdyvehicles)"""
driver.quit()