# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:45:32 2021

@author: anshu
"""

# using flask for building a webservice

from flask import Flask, request
import numpy as np
import json

app = Flask(__name__)

# decorate a method using app decorator
@app.route("/",methods=['GET','POST'])
def main():
    return "Hello World form Flask"

@app.route("/predict",methods=['GET','POST'])
def main2():
    data = request.data
    data = data.decode() # byte to string
    print(data)
    data = json.loads(data)# string to dict
    data['EMP_ID'] = np.random.randint(100,999)
    data['message'] = "Congratualtions!, you are registered now"
    data = json.dumps(data)
    return data

if __name__=="__main__":
    app.run(debug=True)