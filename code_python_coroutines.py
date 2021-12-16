# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:39:26 2021

@author: anshu
"""

# creating a coroutine

def get_greeting(keyword):
    print(f"Searrching for a keyword {keyword}")
    while True:
        greet = (yield)
        if keyword in greet:
            print("Hey hello, Good morning")
            
            
# calling the coroutine
agent = get_greeting("alexa")

# start the coroutine 
# it will execute first line - line number 11
# it will now keep wating for input at line number 13

agent.__next__() # optional, next(agent)

# sending inputs - corresponding to greet = (yield)
agent.send("Hey siri")
agent.send("hey alexa")
agent.send("how are you alexa")
agent.send("hi how are you")


agent.close()

###################################################

text = "I love coding in python, python is amazing and awesome. I hate typing codes and it is hard to remember rules, python is good language."
plist = ['love','happy','awesome','amazing','good']
nlist = ['hate','bad','sad','worst','poor','hard']

# Pipeline by chaining coroutines in python

def data_source(text,next_coroutine):
    word_list = text.split(" ")
    for word in word_list:
        next_coroutine.send(word)
    next_coroutine.close()
    
    
def data_processing(plist=plist,nlist=nlist,next_coroutine=None):
    print("Scanning text data")
    while True:
        word = (yield)
        if word in plist:
            next_coroutine.send([word,'positive'])
        elif word in nlist:
            next_coroutine.send([word,'negative'])

def data_sink():
    print("I am a sink to print final output")
    pcount = 0
    ncount = 0
    while True:
        word = (yield)
        if word[1]=='positive':
            pcount +=1
            print("Positive words count - ",pcount)
        elif word[1]=='negative':
            ncount +=1
            print("Negative words count - ",ncount)
        print(word)
        
ds = data_sink()
ds.__next__()
dp = data_processing(next_coroutine=ds)
dp.__next__()

text = "I love coding in python, python is amazing and awesome. I hate typing codes and it is hard to remember rules, python is good language."
data_source(text, dp)
