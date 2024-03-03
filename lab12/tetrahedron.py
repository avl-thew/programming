import math
import tkinter as tk

class Tetrahedron:
    # Функция для расчета параметров тетраэдра 
    def calculate_tetrahedron(root, a, density):
        V = (a**3) / (6 * math.sqrt(2)) 
        S = math.sqrt(3) * (a**2)
        m = V * density
        return V, S, m