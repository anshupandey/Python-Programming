# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:20:22 2021

@author: Nitu
"""

# random - built in module in python

import random
# generate random numbers
random.random()

# generate a random integer
random.randint(12, 45)

# choose a random entity from a list
m = [2,4,5,6,7,8,9,1,3,4]
random.choice(m)

# choosing k random values from a population->sequence
random.sample(m, 2)

# randomly shuffling the list/sequence
random.shuffle(m)
print(m)

# seeding the randomness - fixing the randomness
random.seed(7)
random.randint(12, 45)

#####################################################
####################################################

import time

time.ctime()

print("hii")
time.sleep(4)
print("Hello")

print(time.timezone)


import datetime as dt
dt.datetime.now()
print(dt.datetime.now())

dt.date(2021, 6, 1)

import calendar
yy = 2021
mm = 6
print(calendar.month(yy,mm))
print(calendar.calendar(2021))
#####################################
#####################################
print(dt.datetime.utcnow())
import pytz
tz = pytz.timezone("Asia/Kolkata")
print(dt.datetime.now(tz))

#########################################################################
#########################################################################
# requests 

import requests
url = "https://api.github.com"
response = requests.get(url)
response.status_code

if response.status_code==200:
    print("successful request")
else:
    print('SOme Error')
    
# fetching the content of response
response.content
# fetching the text from response
response.text

# fetching the informaiton in structured format - json
response.json()

# fetching meta information about the response from server
response.headers
response.headers['Date']
response.headers['Content-Type']


## Query parameter
url = "https://api.github.com/search/repositories"
response= requests.get(url,
                       params={'q':'requests+language:python'})

response.json()

repo = response.json()['items'][1]
repo
print(repo['name'])
print(repo['description'])

##########################################

url = "https://api.github.com/search/repositories"
response= requests.get(url,
                       params={'q':'requests+language:python'},
                       headers={'Accept':'application/json'})


response.json()
################################################################################

## google search
url = "https://www.google.co.in"
query = {'q':'Mumbai'}
response = requests.get(url,params=query)

response.content
response.url

################################################
# Bing seearch
endpoint = "https://api.bing.microsoft.com/v7.0/search"
key = "3552e53d9db54ab5b63d3589a831af01"

headers = {"Ocp-Apim-Subscription-Key":key}
params = {"q":"Mumbai","textDecorations":"true",
          "textFormat":"raw"}

response = requests.get(endpoint,
                        headers=headers,params=params)
response.raise_for_status()

result = response.json()

result.keys()
result['queryContext']
result['webPages']
result['entities']
result['entities']['value'][0]['description']
