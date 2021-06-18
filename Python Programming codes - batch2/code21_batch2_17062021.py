# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:29:19 2021

@author: Nitu
"""

import sqlite3

# create a database / connect to existing database
conn = sqlite3.connect(r"C:\Users\Nitu\Desktop\Python\Batch2\mydb123.db")
# create a table in the database

conn.execute('create table customers (name text, age text, city text, email text, eid text)')

conn.row_factory = sqlite3.Row

cur = conn.cursor()
cur.execute("select * from customers")
rows = cur.fetchall()
print(rows)
for i in rows:print(list(i))


status = cur.execute('insert into customers (name,age,city,email,eid) values (?,?,?,?,?)',
                    ('Max',"45","Kochi","max@max.com",'12345'))

cur.lastrowid
