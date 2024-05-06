import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)

def yk(t, x):
    y = f(t) + f_pr(t) * (x - t)
    return y

tochka_kasaniya = 0.2
h = float(input())
h = round(1/h)
x = np.linspace(0,1,h)
y = []
for i in x:
    y.append(f(i))
x1 = np.array([0.0, 1.0])

plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y)
plt.plot(x1, [yk(tochka_kasaniya, xi) for xi in x1])
plt.plot(tochka_kasaniya, f(tochka_kasaniya), "ro")

plt.show()


