# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:26:41 2021

@author: anshu
"""

# data scrapping using beautifulsoup


import requests

page = requests.get("https://en.wikipedia.org/wiki/Web3")
page

page.status_code

# fetch the content of the page
page.content

##############################################

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

#############################################################

list(soup.children)
len(list(soup.children))

[type(item) for item in list(soup.children)]

# Doctype - info about type of document
# NavigableString = text found in the document
# Tag = other nested tags

# accessing the main content with in the tags
content = list(soup.children)[2]

len(list(content))
list(content)[3]

# accessing body of the page
body = list(content)[3]

list(body.children)

len(list(body.children))
list(body.children)[4]

######################################################

# get all intances of a tag 

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all('p')

len(soup.find_all('p'))

for para in soup.find_all('p'):
    print(para.get_text())
    
    
#################################

url = "https://forecast.weather.gov/MapClick.php?lat=27.857240000000047&lon=-97.64720999999997#.YcLwNWhByUk"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

seven_day_data = soup.find(id='seven-day-forecast-container')

seven_day_data

forecast = seven_day_data.find_all(class_="tombstone-container")

len(forecast)

print(forecast[0].prettify())

forecast[0].find(class_="period-name").get_text()

forecast[0].find(class_="short-desc").get_text()

forecast[0].find(class_="temp").get_text()

# exercise - write code to store this seven day data to a dataframe

period = [fr.find(class_='period-name').get_text() for fr in forecast]
desc = [fr.find(class_='short-desc').get_text() for fr in forecast]
temp = [fr.find(class_='temp').get_text() for fr in forecast]

import pandas as pd
df = pd.DataFrame({'Period':period,'Description':desc,'Temperature':temp})
df

df.to_excel("weather_forecastdata.xlsx")
