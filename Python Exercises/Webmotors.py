import time 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

# 1 - Catch HTML content through URL
url = "https://www.webmotors.com.br/carros-usados/estoque?inst=header:webmotors:header-deslogado::carros-usados-ou-seminovos"

option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)
element = driver.find_element_by_xpath("//div[@class='ContainerCardVehicle ']")
html_content = element.get_attribute('outerHTML')

print(element)

# 2 - Parsing HTML
# 3 - Structure data through Dataframe Pandas
# 4 - Change data to Dictionary
driver.quit()