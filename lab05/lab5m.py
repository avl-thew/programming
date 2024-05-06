
# import math 
# import seaborn as sns 
# import numpy as np 
# import matplotlib.pyplot as plt

# def f(x): 
#     return math.cos(x) * math.exp(-x*x) 
# def f_pr(x): 
#     return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x) 


# def yk(t, x): 
#     y1 = [] 
#     for i in x: 
#         y1.append(f(t) + f_pr(t) * (i - t)) 
#     return y1
        
# tochka_kasaniya = 0.2 
# h = float(input()) 
# h = round(1/h) 
# x = np.linspace(0,1,h) 
# y = [] 
# for i in x: 
#     y.append(f(i)) 

# x1 = np.array([0.0, 1.0])
# sns.set(style="whitegrid")        
# fig, ax = plt.subplots(figsize=(8, 6))  
# sns.lineplot(x=x, y=y, ax=ax, label='f(x)')         
# sns.lineplot(x1=x1, yk=(tochka_kasaniya, x1), ax=ax, label='yk(t, x)')       
# ax.plot(tochka_kasaniya=tochka_kasaniya, f(tochka_kasaniya), label='Точка касания') 
# ax.set_title('График') 
# ax.set_xlabel('x') 
# ax.set_ylabel('y') 
# ax.grid(True)
# ax.legend() 
            
# plt.show()

import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)

def yk(t, x):
    y = f(t) + f_pr(t) * (x - t)
    return y

tochka_kasaniya = 0.2
h = float(input("Введите шаг: "))
h = round(1/h)
x = np.linspace(0, 1, h)
y = [f(i) for i in x]
x1 = np.array([0.0, 1.0])

sns.set()
# fig, ax = plt.subplots()
plt = sns.lineplot(x=x, y=y)
plt = sns.lineplot(x=x1, y=[yk(tochka_kasaniya, xi) for xi in x1])
plt = sns.scatterplot(x=[tochka_kasaniya], y=[f(tochka_kasaniya)], color='red')

plt.set_title('График')
plt.set(xlabel='x', ylabel='y')
plt.grid(True)

# fig.tight_layout()
plt.show()

