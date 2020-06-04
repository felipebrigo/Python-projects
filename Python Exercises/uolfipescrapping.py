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
from selenium.webdriver.common.action_chains import ActionChains

# 1 - Catch HTML content through URL
url = "https://www.uol.com.br/carros/tabela-fipe"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
element=driver.find_element_by_xpath("//div[@class ='fipe-table-page']")
html_content=element.get_attribute('outerHTML')

soup=BeautifulSoup(html_content,'html.parser')
print(soup.prettify())

print(("-"*15))

only_select_tags=SoupStrainer("select")
soup1=BeautifulSoup(html_content,'html.parser',parse_only=only_select_tags)
print(soup1.prettify())

print(("-"*15))

for a in soup1.find_all("select", "target"):
    print(a.get_text())

elementclickable = driver.find_element_by_xpath("//select[@class='target']")
all_options = elementclickable.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))

menu=driver.find_element_by_xpath('//*[@id="ads-interesse"]')
actions=ActionChains(driver)
position=menu.location_once_scrolled_into_view
print(position)
time.sleep(1)
actions.move_by_offset(position)
time.sleep(1)
actions.perform()
actions.move_to_element(menu).click()
time.sleep(1)
actions.perform()
time.sleep(2)

#Não deu certo o codigo daqui para frente. Tentar com Action Chains e se não der, tentar com um click na posição do objeto na página
#vender=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//select[@class='target']")))
#select=Select(vender)
# As duas linhas acima passaram no compilador mas não selecionaram e nem abriram o dropdown box.
#print(select)
#select.select_by_visible_text("Vender")
#vender.click()

"""select=Select(driver.find_element_by_css_selector('select.target').click())
select.select_by_visible_text("Comprar").click()
time.sleep(3)


vender=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id ='ads-interesse')]")))
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
#driver.quit()