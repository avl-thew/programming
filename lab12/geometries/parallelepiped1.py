import tkinter as tk



class Parallelepiped:

    def __init__(self):

        self.base_length = None
        self.base_width = None
        self.height = None
        self.material = None

    def calculate_volume(self):

        print(self.base_length)
        print(self.base_width)
        print(self.height)
        return self.base_length * self.base_width * self.height

    def calculate_surface_area(self):

        return 2 * (self.base_length * self.base_width + self.base_length * self.height + self.base_width * self.height)

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


class ParallelepipedGUI:

    def __init__(self, root):

        self.root = root

        self.parallelepiped = Parallelepiped()


        self.label1 = tk.Label(self.root, text="Base Length")
        self.label1.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()


        self.label2 = tk.Label(self.root, text="Base Width")
        self.label2.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        self.label3 = tk.Label(self.root, text="Height")
        self.label3.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.volume_label = tk.Label(self.root, text="Volume:")
        self.volume_label.pack()

        self.surface_area_label = tk.Label(root, text="Surface Area:")
        self.surface_area_label.pack()

        self.mass_label = tk.Label(root, text="Mass:")
        self.mass_label.pack()

    def calculate(self):

        self.parallelepiped.base_length = float(self.entry1.get())
        self.parallelepiped.base_width = float(self.entry2.get())
        self.parallelepiped.height = float(self.entry3.get())
        self.parallelepiped.material = float(self.entry4.get())


        volume = self.parallelepiped.calculate_volume()
        surface_area = self.parallelepiped.calculate_surface_area()
        mass = self.parallelepiped.calculate_mass()

        self.volume_label.config(text="Volume: {}".format(volume))
        self.surface_area_label.config(text="Surface Area: {}".format(surface_area))
        self.mass_label.confing(text="Mass: {}".format(mass))
        

root = tk.Tk()
gui = ParallelepipedGUI(root)
root.mainloop()









# class Parallelepiped:

#     def __init__(self, length, width, height, material):

#         self.length = length

#         self.width = width

#         self.height = height

#         self.material = material



#     def calculate_volume(self):

#         return self.length * self.width * self.height



#     def calculate_surface_area(self):

#         return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)



#         def calculate_mass(self):
#             #расчет массы в зависимости от материала
#             if self.material == 'сталь':
#                 density = 7850 #плотность стали
#             elif self.material == 'дерево':
#                 density = 800 #плотность дерева
#             else:
#                 density = 0
#             # масса = плотность * объем
#             mass = density * self.calculate_volume() 
#             return mass

