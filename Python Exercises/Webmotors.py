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
url = "https://www.webmotors.com.br/carros/sp?estadocidade=S%C3%A3o%20Paulo&tipoveiculo=carros&precoate=30000&o=5"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
seconds=60
while seconds != 0:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    seconds=seconds-1
element = driver.find_element_by_xpath("//div[@class='Search-result Search-result--container-right']")
html_content=element.get_attribute('outerHTML')

# 2 - Parsing HTML
#soup=BeautifulSoup(html_content,'html.parser')
only_a_tags=SoupStrainer("a")
soup1=BeautifulSoup(html_content,'html.parser',parse_only=only_a_tags)
 
#print(soup1.prettify())

marcas=[]
modelos=[]
valores=[]
anos=[]
for marca in soup1.find_all('h2'):
    #print(marca.get_text())
    marcas.append(marca.get_text())

for modelo in soup1.find_all('h3'):
    #print(modelo.get_text())
    modelos.append(modelo.get_text())

for valor in soup1.find_all(re.compile('^strong')):
    if valor.text != " Santander":
        #print(valor.get_text())
        valores.append(valor.get_text())

for ano in soup1.find_all(re.compile('^span')):
    if ano.text:
        if ano.text != "Home":
            if ano.text != "Carros":
                if ano.text != "Sp":
                    anos.append(ano.get_text())
carrolink=[]
carrolink1=[]    
for link in soup1.find_all('a'):
    comparator=link.get('href')
    word='comprar'
    if comparator.find(word) != -1:
        if comparator != carrolink1:
            carrolink1=comparator
            carrolink.append(carrolink1)
            

# 3 - Structure data through Dataframe Pandas
lista = pd.DataFrame(np.array(anos).reshape(-1,3))
lista.columns=['Ano','kms','Cidade']
df = pd.DataFrame({'Marca': marcas, 'Modelo': modelos, 'Valor': valores, 'Link': carrolink})

result=pd.concat([df,lista],axis=1)
print(result)

# 4 - Export DataTable to Excel or CSV

driver.quit()

result.to_csv(r'/Users/mac/Desktop/Dataframe.csv')