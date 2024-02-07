import tkinter as tk

from geometries import parallelepiped1, tetrahedron1, sphere1



class MainGUI:

    def __init__(self, root):

        self.root = root

        

        self.label = tk.Label(self.root, text="Select a Shape:")

        self.label.pack()

        

        self.shape_var = tk.StringVar()

        

        self.shape_radio1 = tk.Radiobutton(self.root, text="Parallelepiped", variable=self.shape_var, value="parallelepiped")

        self.shape_radio1.pack()

        

        self.shape_radio2 = tk.Radiobutton(self.root, text="Tetrahedron", variable=self.shape_var, value="tetrahedron")

        self.shape_radio2.pack()

        

        self.shape_radio3 = tk.Radiobutton(self.root, text="Sphere", variable=self.shape_var, value="sphere")

        self.shape_radio3.pack()

        

        self.label1 = tk.Label(self.root, text="Material")

        self.label1.pack()

        self.entry1 = tk.Entry(self.root)

        self.entry1.pack()

        

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)

        self.calculate_button.pack()

        

        self.volume_label = tk.Label(self.root, text="Volume:")

        self.volume_label.pack()

        

        self.surface_area_label = tk.Label(self.root, text="Surface Area:")

        self.surface_area_label.pack()

        

        self.mass_label = tk.Label(self.root, text="Mass:")

        self.mass_label.pack()

        

    def calculate(self):

        shape = self.shape_var.get()

        material = self.entry1.get()


        if shape == "parallelepiped":

            p = parallelepiped1.Parallelepiped()

            p.material = material

            volume = p.calculate_volume()

            surface_area = p.calculate_surface_area()

            mass = p.calculate_mass()

            self.volume_label.config(text="Volume: {}".format(volume))

            self.surface_area_label.config(text="Surface Area: {}".format(surface_area))

            self.mass_label.config(text="Mass: {}".format(mass))

            

        elif shape == "tetrahedron":

            t = tetrahedron1.Tetrahedron()

            t.material = material

            volume = t.calculate_volume()

            surface_area = t.calculate_surface_area()

            mass = t.calculate_mass()

            self.volume_label.config(text="Volume: {}".format(volume))

            self.surface_area_label.config(text="Surface Area: {}".format(surface_area))

            self.mass_label.config(text="Mass: {}".format(mass))

        

        elif shape == "sphere":

            s = sphere1.Sphere()

            s.material = material

            volume = s.calculate_volume()

            surface_area = s.calculate_surface_area()

            mass = s.calculate_mass()

            self.volume_label.config(text="Volume: {}".format(volume))

            self.surface_area_label.config(text="Surface Area: {}".format(surface_area))

            self.mass_label.config(text="Mass: {}".format(mass))

        

root = tk.Tk()

gui = MainGUI(root)

root.mainloop()