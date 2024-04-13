# import sympy
# from sympy.abc import x

# f = 1/(x*((x+1)**2))
# print(sympy.integrate(f, (x, 1, 2)))

import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 2
n = 7

def f(x):
    return 1/(x*(x+1)**2)

x = np.linspace(a, b, 100)
y = f(x) 

h = (b-a)/n
xs = np.linspace(a, b, n+1)
ys = f(xs)

plt.plot(x, y, color='red')

for i in range(n):
    xk = a + i*h 
    yk = abs(ys[i])
    plt.gca().add_patch(plt.Rectangle((xk, 0), h, yk, color='green'))
    if ys[i] < 0:
        plt.gca().add_patch(plt.Rectangle((xk, -yk), h, -yk, color='green'))
        
plt.title('График функции и прямоугольники')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
