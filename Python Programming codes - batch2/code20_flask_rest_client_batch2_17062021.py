# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:13:50 2021

@author: Nitu
"""

import requests
import json

data = {"Name":"ANshu",
        "Age":45,
        'Laptop':"banana"}

data = json.dumps(data)
server = "http://127.0.0.1:5000/req"
response = requests.post(server,data)
print(response.text)