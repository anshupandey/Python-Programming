# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:13:36 2021

@author: aspdi
"""

#Client code

import requests
import json
data = {"Name":'Anshu','Age':24,'City':'Delhi'}
data = json.dumps(data)
url = "http://127.0.0.1:5000/predict"

response = requests.post(url,data)
print(response.status_code)
print(response.content)