# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:03:16 2018

@author: 24048
"""

import matplotlib.pyplot as plt
from sympy import *

e = 5e-5

def fun(x):
    return x**3 - x - 1

def Derfrom(i):
    x = symbols("x")
    y = x**3 - x - 1
    dify = diff(y,x)
    return dify.subs('x',i)

def calculate():
    x_0 = 8
    x_new = 3
    err = abs(x_0-x_new)
    while True:
        if err<e:
            return x_new
        x_new = x_0 - fun(x_0)/int(Derfrom(x_0))
        err =abs(x_0 - x_new)
        x_0 = x_new
        print("迭代后:"+str(x_0)+" ")
            
print(calculate())