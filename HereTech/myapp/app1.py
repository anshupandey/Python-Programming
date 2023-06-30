# pip install flask
from flask import Flask, render_template

app = Flask(__name__)


# create a function to be triggered when a request is received on a route

@app.route("/")
def main1():
    return render_template("index.html")


@app.route("/v3")
def main2():
    return "Greetings from Python Version 3.xx"

@app.route("/contact")
def main3():
    return "<h1><center> Welcome to the Dashboard </center></h1>"

if __name__=="__main__":
    app.run()

