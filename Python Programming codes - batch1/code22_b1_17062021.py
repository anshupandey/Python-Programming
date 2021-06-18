# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:25:18 2021

@author: Nitu
"""
from urllib.request import urlopen

data = urlopen("http://127.0.0.1:8000/contact").read()
print(data)


###################################

import requests
url = "https://djangobook.com/wp-content/uploads/mtv_drawing2_new.png"
response = requests.get(url)
with open("myimage.png",'wb') as file:
    file.write(response.content)
    

################## Static method in python

class calc:
    y = 5
    def abc(self):
        self.y = 6
        
    @staticmethod
    def cm2m(x):
        self.y = 8
        return x/100

calc.cm2m(100)

m = calc()
m.cm2m(23)
m.abc()
m.y
#########################################################
# immutable class in python 
from dataclasses import dataclass
@dataclass(frozen=True)
class abcd:
    x = 8
    y = 9
    
    
k = abcd()

k.m = 4
