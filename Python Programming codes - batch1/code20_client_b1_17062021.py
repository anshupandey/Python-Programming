# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 09:18:55 2021

@author: Nitu
"""
import requests
import json

data = {"Name":"Anshu",
        "Age":25,
        "Laptop":"Orange"}
data = json.dumps(data)
server = "http://127.0.0.1:5000/req"
response = requests.post(server,data)
print(response.text)