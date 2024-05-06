import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)

def yk(t, x):
    y1 = []
    for i in x:
        y1.append(f(t) + f_pr(t) * (i - t))
    return y1

tochka_kasaniya = 0.2
h = float(input())
h = round(1/h)
x = np.linspace(0,1,h)
y = []
for i in x:
    y.append(f(i))
x1 = [0.0, 1.0]

plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
sns.lineplot(x, y)
sns.lineplot(x1, yk(tochka_kasaniya, x1))
plt.plot(tochka_kasaniya, f(tochka_kasaniya), "ro")

plt.show()