# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:23:23 2021

@author: aspdi
"""


from flask import Flask, render_template

# create an app using flask
app= Flask(__name__)



@app.route('/',methods=['GET','POST'])
def main():
    return render_template("index.html")


@app.route('/page2',methods=['GET','POST'])
def main2():
    return "hi from python"

@app.route('/hello/<name>',methods=['GET','POST'])
def main3(name):
    return f"hey hi {name} how are you doing? "

# accepted variables - string, int, float, path
# specifying type of variable
@app.route('/blog/<int:postID>',methods=['GET','POST'])
def main4(postID):
    return "<h1> Blog Number: %d </h1"%(postID)


if __name__=='__main__':
    app.run(debug=True)