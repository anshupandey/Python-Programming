# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:04:02 2021

@author: Nitu
"""
import sqlite3
conn = sqlite3.connect("mydb.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("select * from customers")
rows = cur.fetchall()
print(rows)
list(rows[2])
