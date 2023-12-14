import numpy as np
import matplotlib.pyplot as plt
# Задаем точку A и вектор u
A = np.array([-4, 3])
u = np.array([6, 4])
# Находим коэффициенты прямой
k = -u[0] / u[1]
b = A[1] - k * A[0]
# Создаем массив значений x
x = np.linspace(-10, 10, 100)
# Вычисляем соответствующие значения y
y = k * x + b
# Строим график
plt.plot(x, y, label='y = {}x + {}'.format(k, b))
plt.scatter(A[0], A[1], color='red', label='Точка A')
plt.arrow(A[0], A[1], u[0], u[1], color='blue', width=0.1,
head_width=0.5, length_includes_head=True, label='Вектор u')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Прямая, проходящая через точку A перпендикулярно вектору u')
plt.legend()
plt.grid(True)
plt.show()
# Выводим уравнение прямой
print('Уравнение прямой: y = {}x + {}'.format(k, b))
