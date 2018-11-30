# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:00:31 2018

@author: 24048
"""

from scipy.linalg import solve
from sympy import *
import pandas as pd
import numpy as np
from sympy import *


data = pd.DataFrame([2,6,9,13],columns = {'x'})
data['y'] =[4,8,12,21]

#设拟合 y = a+bx+e
def fun(a,b,x):
     return a+b*x

if __name__ == "__main__":  
    y_average = data['y'].sum()/data['y'].size
    
    x_average = data['x'].sum()/data['x'].size
    
    data['x^2'] = data['x'].apply(lambda x : x**2)
    
    data['xy'] = data['x']*data['y']

    xy_average = data['xy'].sum()/data['xy'].size

    x_sqr_average = data['x^2'].sum()/data['x^2'].size
    
    a=Symbol('a')
    
    b=Symbol('b')
    
    dic  = solve([y_average-b*x_average-a,(xy_average-x_average*y_average)/(x_sqr_average-x_average**2)-b],[a,b])
    
    a = dic.get(a)
    
    b = dic.get(b)
    
    print(fun(a,b,2))