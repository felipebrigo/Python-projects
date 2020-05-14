import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

url= "https://stats.nba.com/players/traditional/"

option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)

time.sleep(10)
driver.find_element_by_xpath("")



# 1 - Catch HTML content through URL
# 2 - Parsing HTML
# 3 - Structure data through Dataframe Pandas
# 4 - Change data to Dictionary
# 5 - Convert and save JSON file

#PIP:
# pip install requests2
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install selenium

driver.quit()