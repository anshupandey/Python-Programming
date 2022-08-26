# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:13:00 2022

@author: admin
"""

class swift:    
    def price(self):
        return 450000
    
    def __str__(self):
        return "Maruti Suzuki Swift Dzire 349"
    
class hyundai:    
    def price(self):
        return 7845421
    
    def __str__(self):
        return "Hyndai i20 grand"

class kia:    
    def price(self):
        return 98654512
    
    def __str__(self):
        return "Kia Seltos"


##############################################


def factory(key):
    dictt = {"swift":swift,
             'hyundai':hyundai,
             'kia':kia}
    return dictt[key]()


s = factory('swift')
type(s)
k = factory('kia')
type(k)
