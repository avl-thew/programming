import tkinter as tk



class Tetrahedron:

    def __init__(self):

        self.base_length = None

        self.material = None

        

    def calculate_volume(self):

        return (2**1/2) * (self.base_length * self.base_length * self.base_length)/12

    

    def calculate_surface_area(self):

        return (3**1/2) * self.base_length * self.base_length

    

    def calculate_mass(self):

        # Implement your mass calculation logic here

        pass



class TetrahedronGUI:

    def __init__(self, root):

        self.root = root

        self.tetrahedron = Tetrahedron()

        

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

        self.tetrahedron.base_length = float(self.entry1.get())

        self.tetrahedron.base_width = float(self.entry2.get())

        self.tetrahedron.height = float(self.entry3.get())

        

        volume = self.tetrahedron.calculate_volume()

        surface_area = self.tetrahedron.calculate_surface_area()

        # Add mass calculation logic here

        

        self.volume_label.config(text="Volume: {}".format(volume))

        self.surface_area_label.config(text="Surface Area: {}".format(surface_area))

        # Update mass label with calculated mass

        

root = tk.Tk()

gui = TetrahedronGUI(root)

root.mainloop()