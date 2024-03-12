from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')
f = 1/(x**2*(1+x**2))

integral = integrate(f, x)
print(integral)

x_values = np.linspace(-5, 5, 100)
y_values = [f.subs(x, x_val) for x_val in x_values]

plt.plot(x_values, y_values, color='blue', label='f(x)')

a1, b1 = -2, -1
x1 = np.linspace(a1, b1, 10) 
y1 = [integral.subs(x, x_val) for x_val in x1]
plt.plot(x1, y1, color='green', label='Integral curve 1')

a2, b2 = 1, 3
x2 = np.linspace(a2, b2, 10)
y2 = [integral.subs(x, x_val) for x_val in x2]  
plt.plot(x2, y2, color='green', label='Integral curve 2')

a3, b3 = -3, -2
x3 = np.linspace(a3, b3, 10)
y3 = [integral.subs(x, x_val) for x_val in x3]
plt.plot(x3, y3, color='green', label='Integral curve 3')

plt.legend()
plt.show()

