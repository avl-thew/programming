from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

f = (x**2 + 3*x + 1) / (2*x - 1)

integral = integrate(f, x)
print("Неопределенный интеграл:", integral)

# Построение графиков
x_vals = np.linspace(-2, 3, 100)
y_vals = f.subs(x, x_vals)

plt.plot(x_vals, y_vals, 'b-', label='f(x)')

# Интегральные кривые
c1 = 0
c2 = 5 
c3 = -3
y1 = integral.subs(x, x_vals) + c1
y2 = integral.subs(x, x_vals) + c2
y3 = integral.subs(x, x_vals) + c3

plt.plot(x_vals, y1, 'g-', label='F1(x)')
plt.plot(x_vals, y2, 'g-', label='F2(x)') 
plt.plot(x_vals, y3, 'g-', label='F3(x)')

plt.legend()
plt.show()


#1
x_vals = np.linspace(-5, 5, 50)
y_vals = [f.subs(x, x_i) for x_i in x_vals]
plt.subplot(2, 2, 1)
plt.plot(x_vals, y_vals)
plt.title('Подынтегральная функция')

# первообразные
F1 = integrate(f, x)
y1 = [F1.subs(x, x_i) for x_i in x_vals]
plt.subplot(2, 2, 2)
plt.plot(x_vals, y1)
plt.title('Первообразная 1')

F2 = integrate(f, (x, 5, x)) 
y2 = [F2.subs(x, x_i) for x_i in x_vals]
plt.subplot(2, 2, 3)  
plt.plot(x_vals, y2)
plt.title('Первообразная 2')

F3 = integrate(f, (x, -2, x))
y3 = [F3.subs(x, x_i) for x_i in x_vals]
plt.subplot(2, 2, 4)
plt.plot(x_vals, y3) 
plt.title('Первообразная 3')

plt.tight_layout()
plt.show()

#2


#3












