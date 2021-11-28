# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:20:22 2021

@author: aspdi
"""

from flask import Blueprint

blueprint = Blueprint("example_blueprint", __name__)

@blueprint.route("/")
def index():
    return "this is an example page"