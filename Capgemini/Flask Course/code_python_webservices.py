# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:38:00 2021

@author: anshu
"""

# Working with webservices

import requests

url = "https://api.zippopotam.us/in/"
zipcode = 110030

# send get request and getting response
response = requests.get(url+str(zipcode))

print(response.content.decode())

print(response.json())
################################

# POST request

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"
data = {
    "userId": 1,
    "id": 1,
    "title": "python is awesome",
    "completed": False
  }

data = json.dumps(data)# dict to json
header = {'Content-Type':'application/json'}

response = requests.post(url,data=data,headers=header)

response.json()

################################################

# put request
url = "https://jsonplaceholder.typicode.com/todos/1"
data = {
    "userId": 1,
    "id": 1,
    "title": "python is awesome",
    "completed": False
  }

response = requests.put(url,json = data)
response.json()

requests.get?
