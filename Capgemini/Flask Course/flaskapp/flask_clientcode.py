# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:48:53 2021

@author: anshu
"""

import requests
import json

data = {"Name":"Anshu","Age":25}
data = json.dumps(data)
url = "http://127.0.0.1:5000/predict"

response = requests.post(url,data)
print(response.status_code)
print(response.content)