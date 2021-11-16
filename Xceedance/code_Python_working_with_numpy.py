# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:11:58 2021

@author: anshu
"""

# =============================================================================
# # Modules & packages for analytics
#
# numpy, scipy = mathematical and scientific computation
# pandas = data import/export, data manipulation, data wrangling
#     data cleaning, data aggregation, statistical analysis
#     
# matplotlib,seaborn = basic & advance data visualization
# plotly, bokeh = interactive data visualization
# statsmodels = advance statistics, time series analysis
# pyspark = big data computation using apache spark
#
# =============================================================================

# =============================================================================
# # Modules & Packages for AI, Machine Learning
# 
# scikit-learn = machine learning, feature selection
# tensorflow, pytorch = Deep Learning & AI
# openCV, imgaug = image processing & computer vision
# NLTK, spaCy, gensim,huggingface = text processing, NLP
# 
# =============================================================================


# =============================================================================
# Application Development & testing
# 
# Flask, Djnago, pyramid = Web Application development
# tkinter, pyqt = desktop GUI app development
# unittest, pytest, doctest = testing
# selenium, pyappium = test automation, mobile testing
# =============================================================================

# Getting started with numpy
x = [4,6,9]
y = [2,3,5]
print(x+y)

# arrays - similar to list, key difference is arrays are of 
# specific type

# Numpy has its own two data types built from lists -
# numpy nd array
# numpy matrix

import numpy as np

x = np.array([4,6,9])
y = np.array([7,8,9])
print(x+y)

x = np.array([[4,5,6],
              [1,5,8],
              [3,1,7]])
print(x)
print(x.shape)
print(x.size)
print(x.max())
print(x.mean())
print(x.min())
print(x.argmin())
print(x.argmax())

# common mathematical operations

np.log10(45600)
np.sin(np.deg2rad(90))
np.sqrt(625)
np.square(45)
np.count_nonzero(x)
np.median(x)

# generate arrays with numpy

# using arange
x = np.arange(start=5,stop=30,step=2)
print(x)

# using linspace
x = np.linspace(start=0,stop=20,num=81)
print(x)

# using ones, zeros
x = np.zeros((4,5))
print(x)

x = np.ones((4,3))
print(x)

## Random numbers with numpy

# uniformly distributed random numbers between 0 to 1
x = np.random.rand(10)
print(x)

# nomrally distirbuted random numbers with mean = 0, std = 1
x = np.random.randn(10)
print(x)

# integer random numbers
x = np.random.randint(20,100,5)
print(x)


# freezing the randomness - seeding the randomness
np.random.seed(5)
x = np.random.randint(20,100,5)
print(x)


#############################################################
# linear algebra with numpy
x = np.array([[4,3,9],[2,5,7],[3,6,1]])
print(x)

# getting inverse of a matrix
np.linalg.inv(x)

# getting determinant of a matrix
np.linalg.det(x)

# getting rank of a matrix
np.linalg.matrix_rank(x)

# solve pair of linear equations

# 4x + 5y = 22
# 5x - 2y = 11

# getting the list of coefficient of variables (x,y)
a= [[4,5],[5,-2]]
# getting list of constants
b = [22,11]

# solving equations to get value of x and y
x,y = np.linalg.solve(a,b)
print(x,y)
