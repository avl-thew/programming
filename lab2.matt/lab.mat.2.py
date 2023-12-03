import matplotlib.pyplot as plt
import numpy as np
import sympy as smp


import math
def f(x):
    if x<0:
        return 1/(x**2)
    else:
        return(math.cos(x+1))
print(f(0))


