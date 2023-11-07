#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *
n = Symbol("n")
def fact(n): 
    if(n==1 or n==0): 
        return 1 
    else: 
        return n*fact(n-1)
    def sequence(n):
        return ((3*(fact(n)) + n**3)/(fact(n) + 3**n))
    def plot_points(m):
        x = np.arange(1, m + 1)
        y = sequence(x)
        # (k, 0) - blue colour
        plt.plot(x, np.zeros_like(x), 'bo', label='$(k, 0)$')
        # (0, x_k) - green color
        plt.plot(np.zeros_like(x), y, 'go', label='$(0, x_k)$')
        # (k, x_k) - red color
        plt.plot(x, y, 'ro', label='$(k, x_k)$')
        lim_value = limit(((3*(fact(n)) + n**3)/(fact(n) + 3**n)), n, oo)
        plt.plot(0, lim_value, 'o', color='orange', label='$(lim)$') # Точка предела
        plt.xlabel('$k$')
        plt.ylabel('$x_k$')
        plt.legend()
        plt.grid()
        plt.show()
    m = 20 # number of points
    plot_points(m)
    a = limit(((3*(fact(n)) + n**3)/(fact(n) + 3**n)), n, oo)
    limit_value = sequence(m) # Вычисляем предел последовательности
    plt.plot(m, limit_value, 'o', color='orange') # Строим точку предела последовательности
    plt.axhline(y=limit_value, linestyle='--', color='orange')
    print(a)