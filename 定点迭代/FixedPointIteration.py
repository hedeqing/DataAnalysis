# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:43:21 2018

@author: 24048
"""


from sympy import *
import matplotlib.pyplot as plt

#2x**2+3x-6=0
def fun(x):
    return (2*x)**0.5
    

def calculate():
    x_temp= 100
    index = 0
    
    while True :
        index+=1
        print("epoch:"+str(index)+"  x_temp ="+str(x_temp)+"  "+" loss = "+str(x_temp-fun(x_temp)))
        if x_temp == fun(x_temp):
            return x_temp
        x_temp = fun(x_temp)
if __name__ == "__main__":
    print(calculate())
      

    
