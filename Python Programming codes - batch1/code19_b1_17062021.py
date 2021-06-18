# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 09:10:33 2021

@author: Nitu
"""
import random
from flask import Flask,request,render_template
import json
import sqlite3

# create a database or connect to exisiting database
#conn = sqlite3.connect("mydb.db")
#conn.execute('create table customers (name text, age text, city text, email text, eid text)')

app = Flask(__name__)

## Developing code for REST API server usign Flask
@app.route("/req",methods=['GET','POST'])
def main():
    data = request.data
    print(data,type(data))
    data = data.decode()#bytes to string
    data = json.loads(data) # string to dict
    data["Eid"] = random.randint(10000,99999)
    data['message'] = "Congratulations, you are registered"
    data = json.dumps(data)
    return data

## Working with variables using flask
@app.route("/hello/<name>",methods=['GET','POST'])
def hello_world(name):
    return "Hey Hello %s , hope you are doing good"%name


# accepted variables - string, int, float, path
@app.route('/blog/<int:postID>',methods=['GET','POST'])
def myblog(postID):
    return "<h1> Blog Number: %d </h1>"%postID
##########################################################
##########################################################

@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template("index.html")

@app.route("/get_data",methods=['GET','POST'])
def get_data():
    data = request.form
    print(data,type(data))
    data = dict(data)
    data['EID'] = random.randint(10000,99999)
    data['message'] = "Registration completed"
    for k in data.keys():
        data[k] = str(data[k])
    with sqlite3.connect("mydb.db") as conn:
        cur = conn.cursor()
        cur.execute("insert into customers (name,age,city,email,eid) values (?,?,?,?,?)",
                    (data['name'],data['age'],data['city'],data['email'],data['EID']))
        conn.commit()
    
    
    return render_template("output.html", data=data)

@app.route("/list",methods=['GET','POST'])
def get_list():
    conn = sqlite3.connect("mydb.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from customers")
    rows = cur.fetchall()
    return render_template("list.html", data=rows)

if __name__=="__main__":
    app.run(debug=True,port=5000)