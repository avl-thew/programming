import math
import tkinter as tk

class Sphere:
    # def __init__(self, density):
    #     self.density = density
    # Функция для расчета параметров шара
    def calculate_sphere(root, R, density):
        V = (4/3) * math.pi * (R**3)
        S = 4 * math.pi * (R**2) 
        m = V * density
        return V, S, m