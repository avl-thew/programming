
# import math
# def f(x):
#     if x<0:
#         return 1/(x**2)
#     else:
#         return(math.cos(x+1))
# print(f(0))


import matplotlib.pyplot as plt
import numpy as np
import sympy as smp
x = smp.symbols('x')
# Объявляем функцию
def f(x):
    return ((x * smp.asin(x))+(smp.sin(2*x**2)))/(smp.sin(x) * (smp.log(1 + 4*x)))

def plot_points():
    x_values = np.linspace(-0.1, 0.1, 300)
    y_values = [f(n) for n in x_values]
    # Строим график
    plt.plot(x_values, y_values, label='f(x)')
    # Вычисление предела
    lim = smp.limit(f(x), x, 0)
    # Изображаем предел точкой
    plt.plot(0, lim, 'o', color='orange', label='Limit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.legend()
    plt.grid()
    plt.show()
plot_points()
# Определение функции
f = ((x * smp.asin(x))+(smp.sin(2*x**2)))/(smp.sin(x)*smp.log(1 + 4*x))
# Вычисление предела
lim = smp.limit(f, x, 0)
print(f'Limit: {lim}')



