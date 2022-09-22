# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:14:40 2022

@author: admin
"""


class connectDB:
    def connect(self):
        print("Connecting to DB...")
        print("Successfull connection!")
        

class readdata:
    def read(self):
        print("reading data .....")
        print("data reading completed")
        

class disconnect:
    def disconnect(self):
        print("Disconnected from DB")
        
        
        
class facadeclass:
    
    def __init__(self):
        self.con = connectDB()
        self.rd = readdata()
        self.dis = disconnect()
        
    def start(self):
        self.con.connect()
        self.rd.read()
        self.dis.disconnect()
        
        
        
o = facadeclass()
o.start()
