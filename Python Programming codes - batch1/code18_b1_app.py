# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:16:24 2021

@author: Nitu
"""

from flask import Flask

app = Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def main():
    return "hello world"

@app.route("/contact",methods=["GET","POST"])
def main2():
    return "please contact us at contact@abcompany.com"


if __name__=="__main__":
    app.run(debug=True)
    