# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:15:07 2021

@author: anshu
"""

import december as dc

help(dc)

dc.myfunction()
dc.spectrum(4,3)
e1 =  dc.employee('Anshu')
e1.age = 45
e1.city = "Jakarta"


def myfun():
    print(" i am a monkey function ")
    
# monkey patching
dc.myfunction = myfun
dc.myfunction()

################################################

import time

time.ctime()

# delay
print("hii")
time.sleep(5)
print("bye")

###############################################
import math

math.sqrt(625)
math.cos(math.radians(0))

math.log10(50000)

#################################################

m = 5 # immutable
w = [4,5,6] # mutable / modifiable
k = "hi" # immutable
def myfun():
    print(w,k) # it will take a refrence of global variable
    m = 8 # here a local variable will be created
    print(m,w,k)
    w.append(45)
    print(w)
    return None

myfun()
print(m)
print(w)
print(k)

x = 5
def myfun2():
    print(x)


myfun2()    

x = 5
y = 6
z = 10
def myfun2():
    global z
    print(x,z)
    y = 12
    z = 5
    print(y,z)


myfun2()    
print(x,y)
print(z)


################################################


# =============================================================================
# numpy, scipy = mathematical and scientific calculations
# pandas = data import , export, data manipulation
#     - data wrangling, basic statistical analysis,
#     data cleaning
#     
# matplotlib,seaborn,plotly = basic to advance data visualization
# 
# scikit-learn = machine learning, data science
# 
# tensorflow, pytorch = deep learning, ai
# 
# NLTK,textblob,spacy, gensim = text processing, natural language processing
# opencv, imgaug = image processing, computer vision
# 
# SQL = pymysql, pandas, sqlite3
# 
# pydocx = doc files
# urllib, requests, = rest Apis, request response
# beautifulsoup = data scrapping
# unittest, pytest, doctest, pyselenium, pyappium  = testing
# 
# ####################
# 
# flask, django, pyramid = web app development
# tkinter, pyqt = desktop GUI app
# pyspark = big data analysis using apache spark
# =============================================================================
















