import math


class Tetrahedron:
    def __init__(self, side, density):
        self.name = 'Тетраэдр'
        self.side = side
        self.density = density

    def calculate(self):
        V = (self.side**3) / (6 * math.sqrt(2))
        S = math.sqrt(3) * (self.side**2)
        m = V * self.density
        return V, S, m
