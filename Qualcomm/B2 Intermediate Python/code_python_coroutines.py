# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:41:46 2022

@author: admin
"""

# Coroutines
# parallelization (not OS based parallelization) based on programming logics


def mycor():
    while True:
        print("Iteration starts")
        a = (yield)
        print(a**2)
    
    
m = mycor()
type(m)

# initialize the coroutine, 
next(m)


m.send(6)

print("Hello World")
m.send(9)
m.send(4)
m.send(9)

m.close()

###################################################################


def personal_assist(name):
    print("waiting for input....")
    while True:
        data = (yield)
        if name in data:
            print("Hey, How may I help you")
            
            
pa = personal_assist("Alexa")

next(pa)

pa.send("hi Siri")

pa.send("hey Alexa")
pa.send("hei heloo Alexa")

####################################################################

text = "Python is an awesome programming language, it amazing and easy i love python"
pw = ['good','awesome','amazing','love']
nw = ['hate','bad','sad','poor']


def source(text,next_cr=None):
    words = text.split(" ")
    for w in words:
        next_cr.send(w)
        
        
def processor_cr(pw = pw, nw = nw, next_cr = None):
    while True:
        w = (yield)
        if w in pw:
            next_cr.send([w,'positive'])
        elif w in nw:
            next_cr.send([w,'negative'])
            
            
def sink_cr():
    pcount= 0
    ncount = 0
    while True:
        data = (yield)
        if data[1]=='positive':
            pcount +=1
        elif data[1]=="negative":
            ncount +=1
        print(data)
        
scr = sink_cr()
scr.__next__()            

pcr = processor_cr(next_cr=scr)    
pcr.__next__()

source(text,next_cr=pcr)
