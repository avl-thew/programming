
# import math
# def f(x):
#     if x<0:
#         return 1/(x**2)
#     else:
#         return(math.cos(x+1))
# print(f(0))

import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *

# Определение функции
def f(x):
    return (2*x)/(x - 7)
# Создание массива значений x
x = np.linspace(-100, 6.9, 200)
# Вычисление значений y для каждого значения x
y = []
for i in x:
    y.append(f(i))
# Построение графика
plt.plot(x, y, linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
x = np.linspace(8.1, 100, 200)
y = []
for i in x:
    y.append(f(i))
# Построение графика
plt.plot(x, y, linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
plt.show()