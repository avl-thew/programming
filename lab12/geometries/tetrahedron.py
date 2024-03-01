import math
class Tetrahedron:
    def init(self, side_length, material):
        self.side_length = side_length
        self.material = material
    def calculate_volume(self):
        return (self.side_length ** 3) / (6 * math.sqrt(2))
    def calculate_surface_area(self):
        return math.sqrt(3) * self.side_length ** 2
    def calculate_mass(self):
        # Добавить расчет массы в зависимости от материала
        if self.material == 'сталь':
            density = 7850 #плотность стали
        elif self.material == 'дерево':
            density = 800 #плотность дерева
        else:
            density = 0

        # масса = плотность * объем
        mass = density * self.calculate_volume() 
        return mass