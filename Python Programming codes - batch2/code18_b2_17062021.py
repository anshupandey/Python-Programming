# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:08:24 2021

@author: Nitu
"""

from flask import Flask

# create a Flask app
app = Flask(__name__)

@app.route("/home",methods=['GET','POST'])
def main():
    return "hello from Flask app"

@app.route("/contact",methods=['GET','POST'])
def main2():
    return "<h1> COntact Us</h1><br>This is the contact page"

#################################################################

## working with variables in flask - <>
@app.route("/home/<name>",methods=["GET",'POST'])
def home(name):
    return "Hello %s , hope you are good today"%name
# allowed data types - string, int, float, path

@app.route("/blog/<int:postID>",methods=["GET","POST"])
def myblog(postID):
    return "<h1> Thi sis Blog Number %d </h1>"%postID

if __name__=="__main__":
    app.run(debug=True)
    
    
    
    