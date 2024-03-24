from sympy import *

# вычисление неопределенного интеграла

x = Symbol('x')
f = (x**3)*sqrt(x**2 + 1)

integral = integrate(f, x)
print(integral)

# from sympy import *
# import numpy as np
# import matplotlib.pyplot as plt

# def f(x):
#     return  (x**3)*(np.sqrt(x**2) + 1)

# def f1(x):
#     y = (np.sqrt(x**2 + 1)*(3 * x4 + x2 - 2))/15
#     return y

# def f2(x):
#     y = (np.sqrt(x**2 + 1)*(3 * x4 + x2 - 2))/15 + 3
#     return y

# def f3(x):
#     y = (np.sqrt(x**2 + 1)*(3 * x4 + x2 - 2))/15 - 3
#     return y


# x = np.linspace(-10, 10, 400)


# plt.plot(x, f(x), color='blue')
# plt.plot(x, f1(x), color='green')
# plt.plot(x, f2(x), color='green')
# plt.plot(x, f3(x), color='green')


# plt.grid(True)


# plt.xlim(-10, 10)
# plt.ylim(-4, 15)  


# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('График функции и кривые')
# plt.legend()


# plt.show()

