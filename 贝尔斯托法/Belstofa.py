# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:07:23 2018

@author: 24048
"""


from scipy.linalg import solve
import numpy as np
a = [1,-3.5,2.75,2.125,-3.875,1.25]
b = ['b0','b1','b2','b3','b4','b5']
c = ['c0','c1','c2','c3','c4','c5']
e  = 0.01
def calculate_B(r,s):
    b[0] = a[0]
    b[1] = a[1] + r*b[0]
    i=2
    while i<6:
        b[i] = a[i]+r*b[i-1]+s*b[i-2]
        i= i+1
    
def calculate_C(r,s):
    c[0] = b[0]
    c[1] = b[1] + r*c[0]
    i=2
    while i<6:
        c[i] = b[i]+r*c[i-1]+s*c[i-2]
        i= i+1
        

if __name__ =="__main__":
    r = -1
    s = -1
    while True:
        calculate_B(r,s)
        calculate_C(r,s)
        b.reverse()
        c.reverse()  
        print("b:"+str(b))
        print("c "+str(c))
        print("r "+str(r))
        print('s '+str(s))
        r_temp, s_temp = solve([[c[2], c[3]], [c[1], c[2]]], [-b[1], -b[0]])
        r = r + r_temp
        s = s + s_temp
        if (abs(r_temp/r)and abs(s_temp/s)) <e:
            print('  r:'+str(r)+"   s:"+str(s))
            break
        calculate_B(r,s)
        calculate_C(r,s)
        