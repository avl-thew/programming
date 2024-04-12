import tkinter as tk
import math


class Parallelepiped:
    def __init__(self, a, b, c, density):
        self.name = 'Параллелепипед'
        self.a = a
        self.b = b
        self.c = c
        self.density = density

    def calculate(self):
        V = self.a * self.b * self.c
        S = 2 * (self.a*self.b + self.b*self.c + self.a*self.c)
        m = V * self.density
        return V, S, m
