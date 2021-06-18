# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:39:15 2021

@author: Nitu
"""

from urllib.request import urlopen
data = urlopen("http://127.0.0.1:8000/contact").read()
print(data)
