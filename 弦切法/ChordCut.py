# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:25:09 2018

@author: 24048
"""
import matplotlib.pyplot as plt

from sympy import *

e = 5e-5

def fun(x):
    return x**3 - x - 1

def calculate():
    """
    return root
    """
    x_0 = 1
    x_1 = 1.7
    while True: 
        if abs(x_1-x_0)<e:
            return x_1
        x_temp = x_1 -fun(x_1)*(x_1-x_0)/(fun(x_1)-fun(x_0))
        x_0,x_1= x_1,x_temp
        
if __name__ =="__main__":    
    print(calculate())
        
        
