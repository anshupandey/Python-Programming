# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:54:22 2021

@author: anshu
"""

# =============================================================================
# # Python Design Pattern- Facade
# Facade method - an interface for multiple sub systems 
#     - it helps in creating a single entry point for multiple steps
# 
# =============================================================================


class warmup:
    def walk(self):
        print("walking....")
        
class exercise:
    def run(self):
        print("running...")
        
        
class relax:
    def sit(self):
        print("sitting...")
        
class workout:
    "Facade class"
    
    def __init__(self):
        self.walking = warmup()
        self.exercise = exercise()
        self.relaxing = relax()
        
    def start(self):
        self.walking.walk()
        self.exercise.run()
        self.relaxing.sit()
        
        
wr = workout()
wr.start()
