import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)
h = float(input())
h = round(1/h)
x = np.linspace(0,1,h)
y = []
for i in x:
    y.append(f(i))
x1 = [0.0, 1.0]
y1 =[]
for i in x1:
    y1.append(f(0.2) + f_pr(0.2) * (i - 0.2))
plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(0.2, 0.941, "ro")
plt.show()

