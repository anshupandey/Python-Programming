# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:05:17 2021

@author: Nitu
"""
# random
import random

# get a random number
random.random()

# get a random integer
random.randint(3, 50)

# select a value randomaly froma  list/tuple
m = [3,4,6,7,9,1,2]
random.choice(m)

# selec a list of values randomly
random.sample(m,3)

# shuffle a list
random.shuffle(m)
print(m)

# random seeding - fixing the randomness
random.seed(4)
random.randint(3, 50)

random.seed(8)
random.choice(m)

random.randrange(0,50,5)
list(range(3,50,5))

#####################################################
#####################################################

import time

print(time.ctime())

print("hii")
time.sleep(5)
print("hellllo")

import datetime as dt
dt.datetime.now()
print(dt.datetime.now())

dt.date.today()

dt.datetime.utcnow()

import calendar
yy = 2021
mm = 6
print(calendar.calendar(yy))
print(calendar.month(yy,mm))

#####################################################
# math
import math
math.exp(100)
math.floor(4.53455)
math.ceil(8.34)
math.log10(10000)

# string
import string
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation

##############################################
#######################################################

import requests

url = "https://api.github.com"
response = requests.get(url)

response.status_code
if response.status_code==200:
    print("Successfull resquest")
    
# get the response in bytes format
response.content

# get the response in string format
response.text

# get the response in json format
response.json()

# fetcing meta information about the response
response.headers
response.headers['Date']
response.headers['Server']
response.headers['Content-Type']

#######################################################

url = "https://api.github.com/search/repositories"

response = requests.get(url,
                        params={'q':'requests+language:python'})


response.status_code
info = response.json()
info.keys()
info['total_count']
len(info['items'])
info['items'][1]
info['items'][1]['name']
info['items'][1]['url']
####################################
response = requests.get(url,
                        params={'q':'requests+language:python'},
                        headers = {'Accept':'application/json'})
response.json()

###############################################################

# GOOGLE SEARCH

url = "https://www.google.co.in"
query = {"q":"Mumbai"}
response = requests.get(url,params=query)
response.content

# Bing server - deploy a resource for search on Azure
url = "https://api.bing.microsoft.com/v7.0/search"
subkey = "0e0e03fca4fa42d6a5409aae2c138925"
params = {"q":"Mumbai",
          "answerCount":10,"cc":'in',
          "textDecorations":"true","textFormat":"raw"}
headers = {"Ocp-Apim-Subscription-Key":subkey}

response = requests.get(url,headers=headers,params=params)
response.raise_for_status()

result = response.json()

result.keys()
result['queryContext']
result['webPages']
result['entities']
result['entities']['value']
result['entities']['value'][0]
result['entities']['value'][0]['description']

dd = result['entities']['value'][0]['description']

with open("responsedata.txt",'w') as file:
    file.write(dd)



#################################################################

# post request
url = "https://httpbin.org/post"
res = requests.post(url,data={"key":"value"})
print(res.status_code)
print(res.text)
print(res.content)

# delete request
url = "https://httpbin.org/delete"
res = requests.delete(url)
print(res.status_code)
print(res.text)


