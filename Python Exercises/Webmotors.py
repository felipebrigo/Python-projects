import time 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import requests
import json
import re

# 1 - Catch HTML content through URL
url = "https://www.webmotors.com.br/carros/sp?estadocidade=S%C3%A3o%20Paulo&tipoveiculo=carros&precoate=30000&o=5"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(5)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)
element = driver.find_element_by_xpath("//div[@class='Search-result Search-result--container-right']")
html_content=element.get_attribute('outerHTML')

# 2 - Parsing HTML
soup=BeautifulSoup(html_content,'html.parser')

print(soup.prettify())

def has_class_span_defined(tag_span):
    return tag_span.has_attr('class')
def has_class_strong_defined(tag_strong):
    return tag_strong.has_attr('class')

for marca in soup.find_all('h2'):
    print(marca.get_text())
for modelo in soup.find_all('h3'):
    print(modelo.get_text())
for valor in soup.find_all(has_class_strong_defined):
    print(valor.get_text())
for ano in soup.find_all(has_class_span_defined):
    print(ano.get_text())    
for link in soup.find_all('a'):
    print(link.get('href'))

    
# 3 - Structure data through Dataframe Pandas

# 4 - Change data to Dictionary
driver.quit()