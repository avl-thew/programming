import math
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)

def yk(t, x):
    return f(t) + f_pr(t) * (x - t)

tochka_kasaniya = 0.2
h = float(input("Введите шаг: "))
h = round(1/h)
x = np.linspace(0, 1, h)
y = [f(i) for i in x]
x1 = np.array([0.0, 1.0])

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(x=x, y=y, ax=ax, label='f(x)')
sns.lineplot(x=x1, y=[yk(tochka_kasaniya, xi) for xi in x1], ax=ax, label='yk(t, x)')
plt.scatter([tochka_kasaniya], [f(tochka_kasaniya)], color='red', label='Точка касания')
ax.set_title('График')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend()
plt.show()
