# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:33:41 2021

@author: anshu
"""

from doctest import testmod


def divide(a,b):
    """
    This function is used to divide a value by another value

    Parameters
    ----------
    a : int/float
        DESCRIPTION.
    b : int/float
        DESCRIPTION.

    Returns
    -------
    c : int/float
        DESCRIPTION.
        
    >>> divide(4,1)
    4.0
    >>> divide(12,3)
    4.0
    >>> divide(10,5)
    2.0
    >>> divide(10.5,3)
    3.5

    """
    c = a/b
    return c

if __name__=='__main__':
    testmod(name='divide',verbose=True)
