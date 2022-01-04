# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:05:56 2021

@author: anshu
"""


# =============================================================================
# # Python design patterns - Facade
#  - a single interface for multiple sub systems
#  - which helps in creating a single entry point for multiple steps
# =============================================================================
 
 
class warmup:
    def walk(self):
        print("walking....")
        
class exercise:
    def run(self):
        print("Running....")

class relax:
    def sit(self):
        print("Sitting....")

# Combining multiple classes in a facade class

class workout:
    "Facade class"
    def __init__(self):
        self.warmup = warmup()
        self.relax = relax()
        self.exercise = exercise()
        
    def start(self):
        self.warmup.walk()
        self.exercise.run()
        self.relax.sit()
        
wr = workout()
wr.start()
