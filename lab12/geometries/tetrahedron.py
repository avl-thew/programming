class Tetrahedron:
    def __init__(self, length, material):
        self.length = length
        
        self.material = material

    def calculate_volume(self):
        return (2**1/2) * (self.length * self.length * self.length)/12

    def calculate_surface_area(self):
        return (3**1/2) * self.length * self.length

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