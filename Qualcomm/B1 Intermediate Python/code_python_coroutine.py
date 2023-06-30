# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:10:01 2022

@author: admin
"""

# Coroutine


def get_greeting(kw = "alexa"):
    print("Searching for keyword")
    while True:
        prompt = (yield)
        if kw in prompt:
            print("hey Hello, Good morning")
            yield prompt
            
            
cr = get_greeting("alexa")

type(cr)

next(cr)
cr.send("hey alexa")
cr.send("hey siri")

cr.send("hey hi alexa")

cr.close()

cr
##########################################################



def source_fun(text,next_cr):
    wordlist = text.split(" ")
    for word in wordlist:
        out = next_cr.send(word)
        next(next_cr)
        print(out)
    

def processor_coroutine(pw=['happy','awesome','amazing'],
                        nw=['bad','sad','poor','worst'],
                        next_cr=None):
    while True:
        word = (yield)
        if word in pw:
            out = next_cr.send([word,'positive'])
            next(next_cr)
            yield out
        elif word in nw:
            out = next_cr.send([word,'negative'])
            next(next_cr)
            yield out
    print("processor coroutine is closed now")



def sink__analysis_coroutine():
    print("I am the final sink coroutine")
    pcount = 0
    ncount = 0
    while True:
        word = (yield)
        if word[1]=='positive':
            pcount +=1
        elif word[1]=='negative':
            ncount +=1
        print(word)
        yield [pcount,ncount]
        
text = "Python is an awesome and amazing programming language, I am happy using python"
text2 = "the food was bad and i feel sad wasting my money being a poor guy"

     
scr = sink__analysis_coroutine()
scr.__next__()
pcr = processor_coroutine(next_cr=scr)
pcr.__next__()

pcr.send('happy')
next(pcr)


scr.send(['happy','positive'])
next(scr)

source_fun(text, next_cr=pcr)   
    
scr.close()    
    
    
    
    
    
    