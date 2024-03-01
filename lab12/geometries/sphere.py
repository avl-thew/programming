import math
class Sphere:
    def init(self, radius, material):
        self.radius = radius
        self.material = material
    def calculate_volume(self):
        return (4/3) * math.pi * self.radius ** 3
    def calculate_surface_area(self):
        return 4 * math.pi * self.radius ** 2
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