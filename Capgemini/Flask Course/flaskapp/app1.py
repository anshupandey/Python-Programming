# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:03:05 2021

@author: anshu
"""

from flask import Flask

app = Flask(__name__)

# decorate a method using app decorator
@app.route("/",methods=['GET','POST'])
def main():
    return "Hello World form Flask"


@app.route("/test",methods=['GET','POST'])
def main2():
    return "hey hi"

# adding variables to flask app
# <> can be used to add variables in path
@app.route("/2021/<name>",methods=['GET','POST'])
def main3(name):
    return f"hey hi {name} hope you are good today"

# permissible types - integer,string,float,path
# specifying type of variable
@app.route("/blog/<int:ID>",methods=['GET','POST'])
def main4(ID):
    return "<h1> Blog Number: %d </h1>"%(ID)

if __name__=="__main__":
    app.run(debug=True)
