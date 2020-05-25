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
url = "https://veiculos.fipe.org.br/"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(3)
element = driver.find_element_by_xpath(
    "//*[(@id = 'front')]//*[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]")
html_content=element.get_attribute('outerHTML')
print(html_content)
driver.quit()