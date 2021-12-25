# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:06:59 2021

@author: anshu
"""

# Numpy
a = [4,5,2]
b = [3,6,7]

print(a+b)

import numpy as np

a = np.array([4,2,9])
b = np.array([9,6,3])
print(a+b)

x = np.array([[4,2,9],[7,8,5],[3,6,8]])
print(x)
type(x)

x.shape
x.size
x.min()
x.max()
x.mean()

###########################################################
np.mean(x)
np.median(x)
np.var(x)
np.std(x)
np.min(x)
np.max(x)
np.sin(np.deg2rad(90))
np.log10(1000)
#########################################################

# generate arrays with numpy
x = np.arange(2,20,3) # start = 2, stop = 20, step = 3
print(x)

x = np.linspace(1,20,39) # start = 1, stop = 20, size = 30
print(x)


x = np.zeros(5)
print(x)

x = np.ones((2,4))
print(x)

##############################################################

# random numbers with numpy

# uniformly distributed random numbers between 0 to 1
x = np.random.rand(10)
print(x)

# normally distributed random numbers with mean = 0, std = 1
x = np.random.randn(10)
print(x)

# integer random numbers
x = np.random.randint(5,30,4)
print(x)

# seeding randomness - fixing the method to generate random num
np.random.seed(7)
x = np.random.randint(5,30,4)
print(x)

#######################################################
# linear algebra

# =============================================================================
# 4x + 3y = 26
# 5x - 2y = 21
# =============================================================================

coef = [[4,3],[5,-2]]
const = [26,21]

np.linalg.solve(coef,const)
