class Parallelepiped:
    def __init__(self, length, width, height, material):
        self.length = length
        self.width = width
        self.height = height
        self.material = material

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def calculate_mass(self):
        #расчет массы в зависимости от материала
        if self.material == 'сталь':
            density = 7850 #плотность стали
        elif self.material == 'дерево':
            density = 800 #плотность дерева
        else:
            density = 0

        # масса = плотность * объем
        mass = density * self.calculate_volume() 
        return mass
