# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:41:43 2021

@author: anshu
"""

class swift:
    def price(self):
        return 500000
    def __str__(self):
        return "Maruti Suzuki Swift"
    
class WagonR:
    def price(self):
        return 400000
    
    def __str__(self):
        return "Maruti Suzuki WagonR"
    
class Brezza:
    def price(self):
        return 1000000
    def __str__(self):
        return "Maruti Suzuki Brezza"
    
sw = swift()
print(f"for the car {sw} the price is {sw.price()}")

wr = WagonR()
print(f"for the car {wr} the price is {wr.price()}")

class car_factory:
    def __init__(self,car=None):
        self.car = car
        
    def show_details(self):
        car = self.car()
        print(f"for the car {car} the price is {car.price()}")
        
        
cf = car_factory(car=swift)
cf.show_details()
cf = car_factory(WagonR)
cf.show_details()
