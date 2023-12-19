import matplotlib.pyplot as plt 
import numpy as np

# определяем f(x)
def f(x):
    return x * np.exp(-x**2)
# определяем уравнение касательной прямой
def tangent_line(x):
    return -np.exp(-1)*(2+x)
# определяем уравнение нормальной прямой
def normal_line(x):
    return np.exp(1) * x + np.exp(1) - np.exp(-1)

x = np.linspace(-2,2,100)
y = f(x)

plt.plot(x,y, label = 'f(x)')
plt.plot(x, tangent_line(x), label = 'Касательная прямая')
plt.plot(x, normal_line(x), label = 'Нормальная прямая')
plt.scatter(-1, f(-1), color = 'r', label = 'точка касания')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('График f(x)')
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()