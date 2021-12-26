# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 19:16:34 2021

@author: anshu
"""

# =============================================================================
# Python Functions
#     - Built-in functions
#     - user defined functions
#     - lambda functions
#     - generator functions
# =============================================================================

x = [4,5,6,2,9]

print(x)
len(x)
type(x)
min(x)
max(x)
sum(x)
sorted(x)
dir(x)
help(sorted)

############################################

def myfunction():
    print("hello from python")
    return None

# calling the function
myfunction()

##########################################

def spectrum(a,b):
    c = a+b
    return c

spectrum(7,5)
spectrum(6) # this will throw error
####################################
# we can make arguments of a function have a default value

def spectrum(a,b=6):
    c = a+b
    return c

spectrum(7,5)
spectrum(3)
######################################
def spectrum(a,b=6):
    """ this function can be used to add two numbers
    Parameters
    ----------
    a : int / float / complex
    b : int / float / complex, optional
        DESCRIPTION. The default is 6.

    Returns
    -------
    c : int / float / complex
    """
    c = a+b
    return c

help(spectrum)
print(spectrum.__doc__)



