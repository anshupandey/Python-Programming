# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:46:01 2021

@author: aspdi
"""

from flask import Flask,request,render_template
import json
import random
import sqlite3

# connect to the database and create a table if not exists
conn = sqlite3.connect("mydb.db")
query = "create table if not exists customers(eid numeric,name text, age numeric, city text, email text)"
conn.execute(query)
conn.close()

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    return render_template("index2.html")

@app.route("/get_data",methods=['GET','POST'])
def main2():
    data = request.form
    print(data,type(data))
    data = dict(data)
    data['EMP_id'] = random.randint(10000,999999)
    data['message'] = "Registration Completed"
    with sqlite3.connect("mydb.db") as conn:
        cur = conn.cursor()
        query = "insert into customers(eid,name,age,city,email) values(?,?,?,?,?);"
        cur.execute(query,(data['EMP_id'],data['name'],int(data['age']),data['city'],data['email']))
        conn.commit()
    return render_template("output.html", data=data)

@app.route("/getlist",methods=['GET','POST'])
def main3():
    conn = sqlite3.connect("mydb.db")
    data = conn.execute("select * from customers")
    return render_template("list.html",data=data)


if __name__=="__main__":
    app.run(debug=True)

