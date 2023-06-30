from turtle import distance
from flask import Flask, render_template, request

import json
import sqlite3

def get_cur():
    conn = sqlite3.connect("city.db")
    cur = conn.cursor()
    return cur,conn

cur,conn = get_cur()
try:
    cur.execute("select * from sqlite_master where type='table';")
    table_list = cur.fetchall()
    if len(table_list)<1:
        cur.execute("create table cities (cityid text primary key, cityname text, citylat text, citylong text);")
        conn.commit()
        conn.close()
except:
    print("table exists")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/storedata",methods=['POST','GET'])
def main2():
    mydata = request.form # fetch the data filled by user on admin page
    mydata = dict(mydata)
    print(mydata,type(mydata))

    # dump the new data to a database
    query = "insert into cities (cityid,cityname,citylat,citylong) values (?,?,?,?);"
    cur,conn = get_cur()
    cur.execute(query,(mydata['cid'],mydata['cname'],mydata['clat'],mydata['clon']))
    conn.commit()
    conn.close()
    return render_template("success.html")
    

@app.route("/explore")
def main3():
    cur,conn = get_cur()
    cur.execute("select * from cities;")
    data = cur.fetchall()
    print(data)
    conn.close()

    return render_template("data.html",output=data)

@app.route("/user")
def main4():
    cur,conn = get_cur()
    cur.execute("select * from cities")
    cdata = cur.fetchall()
    conn.close()
    return render_template("user.html",output=cdata)


import haversine as hs

@app.route("/getDist",methods=['POST','GET'])
def main5():
    udata = request.form
    udata = dict(udata)
    print(udata)
    cur,conn = get_cur()
    cur.execute(f"select citylat,citylong from cities where cityid='{udata['city1']}';")
    lat1,lon1 = cur.fetchall()[0]
    cur.execute(f"select citylat,citylong from cities where cityid='{udata['city2']}';")
    lat2,lon2 = cur.fetchall()[0]
    distance = hs.haversine((float(lat1),float(lon1)),(float(lat2),float(lon2)))
    return "The distance is : "+str(round(distance,2))+' KM <br> <br> <a href="http://127.0.0.1:5000/user> Go back </a>"'

if __name__=="__main__":
    app.run()