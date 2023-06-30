# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:47:38 2022

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
    
# creating abstract method

class car_factory:
    def __init__(self,name):
        self.car = name
        
    def show_details(self):
        car = self.car()
        print(f"the price for car {car} is {car.price()}")
        
c = car_factory(kia)
c.show_details()

c = car_factory(hyundai)
c.show_details()

type(c)
