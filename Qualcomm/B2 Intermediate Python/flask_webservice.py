# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:50:10 2022

@author: admin
"""

from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return "Hello from python"

@app.route("/abc",methods=['GET','POST'])
def main2():
    return "Hello from ME, and python"

if "__main__"==__name__:
    app.run()