import time 
import threading
import string
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import requests
import re
import numpy as np
from selenium.webdriver.common import action_chains

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
#print(soup1.prettify())

#Parse and append all data into a Dataframe
for marcas in soup1.find_all("option"):
    value.append(marcas['value'])
    brand.append(marcas.get_text())
df = pd.DataFrame({'Indice': value, 'Modelo': brand})
df=df.drop(0)
qtdyvehicles=df.shape[0]
print(df)
print(qtdyvehicles)

#Iterate with first combobox selected - to fix code from this point - Difficulty to iterate to dropdown box
brandelements = driver.find_element_by_xpath(
    "//select[(@id = 'selectMarcacarro')]")
html_new_content=brandelements.get_attribute('outerHTML')
print(html_new_content)
select = Select(brandelements)
select.select_by_visible_text('Troller')
brandelements.location_once_scrolled_into_view

newelement=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"selectMarcacarro")))
newelement.click()
time.sleep(2)
action_chains.ActionChains(driver).move_to_element(brandelements).click().perform()
brandelements[0].click()

#select.select_by_value("57")
#select.click()

all_options=brandelements.find_elements_by_tag_name("option")

for option in all_options:
    select = Select(brandelements).select_by_value("127")
    print(select)
    time.sleep(1)
    
yearelement = driver.find_element_by_xpath(
    "//*[(@id = 'selectAnoModelocarro')]")
html_year_element_content=yearelement.get_attribute('outerHTML')
#print(html_year_element_content)
time.sleep(1)

"""element = driver.find_element_by_xpath(
    "//*[(@id = 'selectMarcacarro')]")
html_content=element.get_attribute('outerHTML')
print(html_content)

WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//select[(@id = 'selectMarcacarro')]//options[contains(.,'Troller')]")))
#select.click()
select.select_by_visible_text('Troller')
"""


driver.quit()
