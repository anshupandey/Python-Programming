# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:10:38 2021

@author: Nitu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:08:24 2021

@author: Nitu
"""

from flask import Flask,request, render_template
import json
import random
import sqlite3


# create a Flask app
app = Flask(__name__)

# REST API server using FLask
@app.route("/req",methods=['GET','POST'])
def main():
    data = request.data
    print(data,type(data))
    data = data.decode() # to convert bytes to string
    data = json.loads(data) # string to dict
    data['eid'] = random.randint(10000,99999)
    data['message'] = "congratulations, registration is completed"
    return json.dumps(data)


## Developing a web app with flask
@app.route("/",methods=["GET","POST"])
def hompage():
    return render_template("index.html")

@app.route("/getdata",methods=["GET","POST"])
def nextpage():
    data = request.form
    print(data,type(data))
    data = dict(data)
    data['eid'] = random.randint(10000,99999)
    data['message'] = "congratulations, registration is completed"
    for k in data.keys():
        data[k] = str(data[k])
    with sqlite3.connect("mydb123.db") as conn:
        cur = conn.cursor()
        cur.execute('insert into customers (name,age,city,email,eid) values (?,?,?,?,?)',
                    (data['name'],data['age'],data['city'],data['email'],data['eid']))
        conn.commit()
    return render_template("output.html", data=data)

@app.route("/list",methods=["GET","POST"])
def get_list():
    conn = sqlite3.connect("mydb123.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from customers")
    rows = cur.fetchall()
    return render_template("list.html", data=rows)

if __name__=="__main__":
    app.run(debug=True)
    
    
    
    