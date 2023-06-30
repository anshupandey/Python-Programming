# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:23:23 2022

@author: admin
"""
# =============================================================================
# 
# Facade 
#     - a pattern in which we combine multiple subsystems 
#     together
# =============================================================================



# Database connection

class DBconnect:
    def __init__(self):
        print("DB Connection Started...")
        
    def connect(self):
        print("Connected to database")
        
class fetchdata:
    def fetch(self):
        print("Fetching data from the database ....")
        
        
class disconnect:
    def discon(self):
        print("Disconnecting from the database ...")
        
        
class facade_class:
    def __init__(self):
        self.con = DBconnect()
        self.fetch = fetchdata()
        self.dis = disconnect()
        
    def do_job(self):
        self.con.connect()
        self.fetch.fetch()
        self.dis.discon()

    
f = facade_class()
f.do_job()
