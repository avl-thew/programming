from sympy import *

# вычисление неопределенного интеграла

x = Symbol('x')
f = (x**2 + 3*x + 1) / (2*x - 1)

integral = integrate(f, x)
print( integral)

# import numpy as np
# import math
# import matplotlib.pyplot as plt


# def f(x):
#     return  (x**2 + 3*x + 1) / (2*x - 1)

# def f1(x):
#     y = ((x**4)/4) + ((7*x)/4) + (11/8) + np.log(2*x - 1)
#     return y

# def f2(x):
#     y = ((x**4)/4) + ((7*x)/4) + (11/8) + np.log(2*x - 1) + 3
#     return y

# def f3(x):
#     y = ((x**4)/4) + ((7*x)/4) + (11/8) + np.log(2*x - 1) - 3
#     return y


# x = np.linspace(-10, 10, 400)


# plt.plot(x, f(x), color='blue')
# plt.plot(x, f1(x), color='green')
# plt.plot(x, f2(x), color='green')
# plt.plot(x, f3(x), color='green')


# plt.grid(True)


# plt.xlim(-10, 10)
# plt.ylim(-15, 15)  


# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('График функции и кривые')
# plt.legend()


# plt.show()