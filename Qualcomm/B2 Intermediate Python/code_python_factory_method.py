# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:03:47 2022

@author: admin
"""

class switft:
    def price(self):
        return 5000000    
    def __str__(self):
        return "Maruti Suzuki Swift VDI"

class hyundai:
    def price(self):
        return 2554110    
    def __str__(self):
        return "Hyundai i10 grand"


class kia:
    def price(self):
        return 486432000    
    def __str__(self):
        return "Kia Seltos"
    
    
h = hyundai()
print(f"the price for car {h} is {h.price()}")

k = kia()
print(f"the price for car {k} is {k.price()}")


def factory(otype):
    "factory method"
    mydb = {"swift":switft,
            "kia":kia,'hyundai':hyundai}
    return mydb[otype]()
    

k = factory("kia")
type(k)
s = factory("swift")    
type(s)    
print(f"the price for car {k} is {k.price()}")
    
    