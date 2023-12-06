
# import math
# def f(x):
#     if x<0:
#         return 1/(x**2)
#     else:
#         return(math.cos(x+1))
# print(f(0))

import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *
# Определение символа x
x = Symbol ('x')
def f(x):
    if x < 0:
        return 1/(x**2)
    else:
        return(np.cos(x+1))
# Создание массива значений x около точки разрыва
x0 = np.linspace(-0.2 * np.pi, 0.2 * np.pi, 100)
y0 = []
for i in x0:
    y0.append(f(i))
# Построение графика
plt.plot(x0, y0)
plt.axvline(x=0, color='red', linestyle='--', label='x=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x)')
plt.legend()
plt.grid()
plt.show()
f1 = 1/(x**2)
lim_left = limit(f1, x, 0, dir='-')
# по умолчанию вычисляется предел справа
f2 = cos(x+1)
lim_right = limit(f2, x, 0)
print(f'Предел слева в точке x=0: {lim_left}')
print(f'Предел справа в точке x=0: {lim_right}')