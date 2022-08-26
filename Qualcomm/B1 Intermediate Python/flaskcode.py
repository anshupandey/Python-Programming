# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:11:10 2022

@author: admin
"""

from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello from python"

@app.route("/abc",methods=['GET','POST'])
def main2():
    return "<center><h1> Welcome to Dashboard</h1>"

if "__main__"==__name__:
    app.run(host="0.0.0.0",port = 9500)
    