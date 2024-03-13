

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')
f = 1/(x**2*(1+x**2))

integral1 = integrate(f, x)
print(integral1)

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




from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')
f = (x**3)*sqrt(x**2 + 1) 

integral = integrate(f, x)
print(integral)

x_values = np.linspace(-1, 1, 100)
y_values = [f.subs(x, x_values) for x_values in x_values]

plt.subplot(2, 2, 1)
plt.plot(x_values, y_values)
plt.title('Подынтегральная функция')



plt.plot(x_values, y_values, color='blue')
# первообразные
F1 = integrate(f, x)
y1 = [F1.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 2)
plt.plot(x_values, y1)
plt.title('Первообразная 1')

F2 = integrate(f, (x, 5, x)) 
y2 = [F2.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 3)  
plt.plot(x_values, y2)
plt.title('Первообразная 2')

F3 = integrate(f, (x, -2, x))
y3 = [F3.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 4)
plt.plot(x_values, y3) 
plt.title('Первообразная 3')

plt.tight_layout()
plt.show()



from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

f = (x**2 + 3*x + 1) / (2*x - 1) 

integral = integrate(f, x)
print("Неопределенный интеграл:", integral)

x_values = np.linspace(-3, 3, 100)
y_values = [f.subs(x, x_values) for x_values in x_values]

plt.plot(x_values, y_values, color='blue', label='f(x)')

plt.subplot(2, 2, 1)
plt.plot(x_values, y_values)
plt.title('Подынтегральная функция')


plt.plot(x_values, y_values, color='blue')
# первообразные
F1 = integrate(f, x)
y = [F1.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 2)
plt.plot(x_values, y)
plt.title('Первообразная 1')

F2 = integrate(f, (x, 5, x)) 
y2 = [F2.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 3)  
plt.plot(x_values, y2)
plt.title('Первообразная 2')

F3 = integrate(f, (x, -2, x))
y3 = [F3.subs(x, x_i) for x_i in x_values]
plt.subplot(2, 2, 4)
plt.plot(x_values, y3) 
plt.title('Первообразная 3')

plt.tight_layout()
plt.show()