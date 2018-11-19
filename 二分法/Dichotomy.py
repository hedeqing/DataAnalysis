# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:37:31 2018

@author:何德庆
"""

import matplotlib.pyplot as plt

a_x = []
a_abs = []
a_y = []
e = 5e-5
def fun(x):
    """
    函数初始化
    param x: 输入
    """
    return 2*x**3+3*x**2-6
def show_fun():
    """
    可视化函数
    """
    b_x= []
    b_y = []
    for i in range(-50,50):
        b_x.append(i)
        b_y.append(fun(i))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(b_x,b_y)
    plt.show()
    
def calculate(a,b):
    """
    逼近函数
    param a :下限值
    param b :上限值
    返回值  x： 近似根
    """
    epoch = 0
    x = (a + b)/2.0
    while True:
        if abs((b-a)/b) < e:
            return x
        if  fun(a)*fun(x)<0:
            b = x
        else:
            a = x
        epoch=epoch+1
        a_x.append(epoch)
        a_abs.append(abs((b-a)/b))
        x = (a+b)/2.0
if __name__ =="__main__":    
    show_fun()
    print(calculate(-5, 5))
    plt.figure(figsize=(10,5))
    plt.xlabel("epoches")
    plt.ylabel('abs')
    plt.plot(a_x, a_abs,label='abs',color='red')
    plt.show()
