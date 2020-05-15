import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

# 1 - Catch HTML content through URL
url= "https://stats.nba.com/players/traditional/?sort=PLAYER_NAME&dir=1"

option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

driver.find_element_by_xpath("//div[@class ='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

element=driver.find_element_by_xpath("//div[@class ='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

print(html_content)

# 2 - Parsing HTML
soup = BeautifulSoup(html_content,'html.parser')
table = soup.find(name='table')

# 3 - Structure data through Dataframe Pandas
df_full = pd.read_html(str(table))[0].head(10)
df=df_full[['Unnamed: 0','PLAYER','TEAM','PTS']]
df.columns = ['pos','player','team','total']
print(df)

# 4 - Change data to Dictionary
top10ranking = {}

top10ranking['points'] = df.to_dict('records')
print(top10ranking)
driver.quit()

# 5 - Convert and save JSON file
js=json.dumps(top10ranking)
fp=open('ranking.json','w')
fp.write(js)
fp.close
