import time 
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import requests
import json
import re
import numpy as np

# 1 - Catch HTML content through URL
url = "https://www.webmotors.com.br/carros/sp?estadocidade=S%C3%A3o%20Paulo&tipoveiculo=carros&precoate=30000&o=5"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(2)
element = driver.find_element_by_xpath("//div[@class='Search-result Search-result--container-right']")
html_content=element.get_attribute('outerHTML')

# 2 - Parsing HTML
soup=BeautifulSoup(html_content,'html.parser')
only_a_tags=SoupStrainer("a")
soup1=BeautifulSoup(html_content,'html.parser',parse_only=only_a_tags)
"""
print(soup.prettify())
for marca in soup.find_all('h2'):
    print(marca.get_text())
for modelo in soup.find_all('h3'):
    print(modelo.get_text())
for valor in soup.find_all(re.compile('^strong')):
    if valor.text != " Santander":
        print(valor.get_text())
for ano in soup.find_all(re.compile('^span')):
    if ano.text:
        print(ano.get_text())    
for link in soup.find_all('a'):
    print(link.get('href'))
"""    
print(soup1.prettify())

marcas=[]
modelos=[]
valores=[]
anos=[]
for marca in soup1.find_all('h2'):
    #print(marca.get_text())
    marcas.append(marca.get_text())
print(marcas)
for modelo in soup1.find_all('h3'):
    #print(modelo.get_text())
    modelos.append(modelo.get_text())
print(modelos)
for valor in soup1.find_all(re.compile('^strong')):
    if valor.text != " Santander":
        #print(valor.get_text())
        valores.append(valor.get_text())
print(valores)
for ano in soup1.find_all(re.compile('^span')):
    if ano.text:
        if ano.text != "Home":
            if ano.text != "Carros":
                if ano.text != "Sp":
                    anos.append(ano.get_text())
                    #print(ano.get_text())
print(anos)
"""df["ano","km","cidade-UF"] = ano
for link in soup1.find_all('a', not 'CardVehicle__linkPhoto'):
    print(link.get('href'))
"""

# 3 - Structure data through Dataframe Pandas
lista = pd.DataFrame(np.array(anos).reshape(3,int(len(anos)/3)), columns=['Ano','kms','Cidade'])
print(lista)
df = pd.DataFrame({'Marca': marcas, 'Modelo': modelos, 'Valor': valores})
print(df)

# 4 - Change data to Dictionary
driver.quit()