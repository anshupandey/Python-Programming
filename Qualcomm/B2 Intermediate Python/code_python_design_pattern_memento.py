# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:15:26 2022

@author: admin
"""

# Memento

class memento:
    def __init__(self,file,data):
        self.file = file
        self.data = data
        
class writer:
    def __init__(self,file):
        self.file = file
        self.data = ""
        
    def write(self,text):
        self.data += text
        
    def save(self):
        return memento(self.file,self.data)
    
    def undo(self,mt):
        self.file = mt.file
        self.data = mt.data
        
        
class version_manager:
    def save(self,wrt):
        self.obj = wrt.save()
        
    def undo(self,wrt):
        wrt.undo(self.obj)
        

user = version_manager()

w = writer("mydata.txt")

w.write("hello, hi how are you?")
print(w.data)

user.save(w)
w.write("\n\n I am good, how are you today?")
print(w.data)

user.save(w)

w.write("\n\n I am good, how are you today?")
print(w.data)

user.undo(w)

print(w.data)
