import time 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

# 1 - Catch HTML content through URL
url = "https://www.webmotors.com.br/carros/sp?estadocidade=S%C3%A3o%20Paulo&tipoveiculo=carros&precoate=50000&o=5"

option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)
element = driver.find_element_by_xpath("//div[@class='Search-result Search-result--container-right']")
html_content=element.get_attribute('outerHTML')

#print(html_content)

# 2 - Parsing HTML
soup=BeautifulSoup(html_content,'html.parser')
print(soup.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))
# 3 - Structure data through Dataframe Pandas
# 4 - Change data to Dictionary
driver.quit()