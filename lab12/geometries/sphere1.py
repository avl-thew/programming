import tkinter as tk



class Sphere:

    def __init__(self):

        self.radius = None
        self.material = None


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



class SphereGUI:

    def __init__(self, root):

        self.root = root
        self.sphere = Sphere()

        self.label1 = tk.Label(self.root, text="Base Rarius")
        self.label1.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

    
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.volume_label = tk.Label(self.root, text="Volume:")
        self.volume_label.pack()

        self.surface_area_label = tk.Label(root, text="Surface Area:")
        self.surface_area_label.pack()

        self.mass_label = tk.Label(root, text="Mass:")
        self.mass_label.pack()

    def calculate(self):

        self.sphere.radius = float(self.entry1.get())
        #self.sphere.material = float(self.entry2.get())
        volume = self.sphere.calculate_volume()
        surface_area = self.sphere.calculate_surface_area()
        mass = self.sphere.calculate_mass()

        self.volume_label.config(text="Volume: {}".format(volume))
        self.surface_area_label.config(text="Surface Area: {}".format(surface_area))
        self.mass_label.confing(text="Mass: {}".format(mass))

root = tk.Tk()
gui = SphereGUI(root)
root.mainloop()