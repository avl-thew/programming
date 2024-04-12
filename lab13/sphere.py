import math


class Sphere:
    def __init__(self, R, density):
        self.name = 'Шар'
        self.R = R
        self.density = density

    def calculate(self):
        V = (4/3) * math.pi * (self.R**3)
        S = 4 * math.pi * (self.R**2)
        m = V * self.density
        return V, S, m
