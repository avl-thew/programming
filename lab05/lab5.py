import math
import numpy as np 
import matplotlib.pyplot as plt

# with open('file.txt1', 'r') as file:
#     data = file.readlines()
def f(x):
    return math.log(x +1) - math.sqrt(4 - x*x)
h = float(input())
h = round(2/h)
x = np.linspace(0,2,h)
y = []

x = []
y = []
for line in data:
    line = line.strip().split()
    x.append(float(line[0]))
    y.append(float(line[1]))

x0 = 0
y0 = -1.036


plt.plot(x, y, label='График функции')

plt.axhline(y0,  label='Касательная', color='r', linestyle='--')

plt.title('График функции с касательной, параллельной оси Ox')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

def f(x):
    return math.log(x +1) - math.sqrt(4 - x*x)

def f_pr(x):
    return (1 / (x+1)) + (x / (math.sqrt(4 - x*x)))

h = float(input())
h = round(2/h)
x = np.linspace(0,2,h)
y = []
for i in x:
    y.append(f(i))
x1 = [0.0, 2.0]
y1 = []
m = 1.257
n = -0.046
for i in x:
    y1.append(f(m) + f_pr(m) * (i - m))

plt.title('График функции с касательной')
plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.plot(x,y)
plt.plot(x1, y1)
plt.plot(m, n, "ro")
plt.show()

