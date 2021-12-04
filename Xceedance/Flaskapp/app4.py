# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:22:08 2021

@author: aspdi
"""

from flask import Flask
from ex_blueprint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__=="__main__":
    app.run()