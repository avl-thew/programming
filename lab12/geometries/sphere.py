class Sphere:
    def __init__(self, radius, material):
        self.radius = radius
        
        self.material = material

    def set_material(self, material):
        self.material = material
    
    def set_radius(self, radius):
        self.radius = radius

    def calculate_volume(self):
        return (4/3) * 3.14 * self.radius

    def calculate_surface_area(self):
        return 4 * 3.14 * self.radius * self.radius

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