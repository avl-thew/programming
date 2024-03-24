
from tkinter import *
import tkinter as tk
import parallelepiped, tetrahedron, sphere



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
            print("ВЫБРАН ПАРАЛЕЛЕПИПИД\n")
            print(material)
            p = parallelepiped.Parallelepiped()
            p.material = material
            volume = p.calculate_volume() #ошибка
            surface_area = p.calculate_surface_area()
            mass = p.calculate_mass()
            self.volume_label.config(text="Volume: {}".format(volume))
            self.surface_area_label.config(text="Surface Area: {}".format(surface_area))
            self.mass_label.config(text="Mass: {}".format(mass))

        elif shape == "tetrahedron":
            t = tetrahedron.Tetrahedron()
            t.material = material
            volume = t.calculate_volume()
            surface_area = t.calculate_surface_area()
            mass = t.calculate_mass()
            self.volume_label.config(text="Volume: {}".format(volume))
            self.surface_area_label.config(text="Surface Area: {}".format(surface_area))
            self.mass_label.config(text="Mass: {}".format(mass))

        elif shape == "sphere":
            s = sphere.Sphere()
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













# root = Tk()

# # Создание виджетов

# length_label = Label(root, text="Длина:")

# length_entry = Entry(root)

# width_label = Label(root, text="Ширина:")

# width_entry = Entry(root)

# height_label = Label(root, text="Высота:")

# height_entry = Entry(root)

# calculate_button = Button(root, text="Рассчитать")

# result_label = Label(root)



# # Размещение виджетов на сетке

# length_label.grid(row=0, column=0)

# length_entry.grid(row=0, column=1)

# width_label.grid(row=1, column=0)

# width_entry.grid(row=1, column=1)

# height_label.grid(row=2, column=0)

# height_entry.grid(row=2, column=1)

# calculate_button.grid(row=3, column=0, columnspan=2)

# result_label.grid(row=4, column=0, columnspan=2)



# # Определение функции обработки нажатия на кнопку

# def calculate_volume():

#     length = float(length_entry.get())

#     width = float(width_entry.get())

#     height = float(height_entry.get())

#     material = "wood"  # здесь можно добавить выбор материала

#     parallelepiped = Parallelepiped(length, width, height, material)

#     volume = parallelepiped1.calculate_volume()

#     result_label.configure(text="Объем: " + str(volume))



# calculate_button.configure(command=calculate_volume)



# root.mainloop()