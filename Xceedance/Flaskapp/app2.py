# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:08:13 2021

@author: aspdi
"""

# Using flask for webservice

from flask import Flask, request
import numpy as np
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello from flask"

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.data
    print(data,type(data))
    data = data.decode() # from bytes to string
    data = json.loads(data) # from string to dict
    data['EMP_ID'] = np.random.randint(100,999)
    data['message'] = "Congratulations! you are now registered"
    data = json.dumps(data)
    return data


if __name__=="__main__":
    app.run(debug=True,port=5000)