from tkinter import *
from parallelepiped import Parallelepiped
from tetrahedron import Tetrahedron
from sphere import Sphere

sph = sphere.Sphere(10, "сталь")

def set_entry(entry: Entry, source: Entry):
    sph.set_material("сталь")
    sph.set_radius(int(source.get()))
    entry.insert(0, str(sph.calculate_volume()))

root = Tk()

root.title("Lab 12")
root.geometry('580x300')
root.configure(bg="#232a2f")
root.resizable(width=False, height=False)

sphere = Frame(root, width=220, height=100, padx=10, pady=10)
sphere_label = Label(sphere, text="Сфера")
sphere_label.pack(fill=X, padx=10, pady=10)
sphere_entry_var = ""
sphere_entry = Entry(sphere, width=10, textvariable=sphere_entry_var)
sphere_entry.pack(fill=X, pady=20)
sphere_entry2 = Entry(sphere, width=10)
sphere_entry2.pack(fill=X, pady=20)
sphere_button = Button(sphere, command=lambda x=sphere_entry2: set_entry(x, sphere_entry))
sphere_button.pack(fill=X, pady=20)

sphere.grid(row=1, column=1, padx=30, pady=20)

tetrahedron = Frame(root, width=220, height=100, padx=10, pady=10)
tetrahedron_label = Label(tetrahedron, text="Тетраэдр")
tetrahedron_label.pack(fill=X, padx=10, pady=10)
tetrahedron_entry_var = ""
tetrahedron_entry = Entry(tetrahedron, width=10, textvariable=tetrahedron_entry_var)
tetrahedron_entry.pack(fill=X, pady=20)
tetrahedron_entry2 = Entry(tetrahedron, width=10)
tetrahedron_entry2.pack(fill=X, pady=20)
tetrahedron_button = Button(tetrahedron, command=lambda x=tetrahedron_entry2, y=tetrahedron_entry: set_entry(x, y))
tetrahedron_button.pack(fill=X, pady=20)


tetrahedron.grid(row=1, column=2, padx=30, pady=20)

parallelepiped = Frame(root, width=220, height=100, padx=10, pady=10)
parallelepiped_label = Label(parallelepiped, text="Параллелепипед")
parallelepiped_label.pack(fill=X, padx=10, pady=10)
parallelepiped_entry_var = ""
parallelepiped_entry = Entry(parallelepiped, width=10, textvariable=parallelepiped_entry_var)
parallelepiped_entry.pack(fill=X, pady=20)
parallelepiped_entry2 = Entry(parallelepiped, width=10)
parallelepiped_entry2.pack(fill=X, pady=20)
parallelepiped_button = Button(parallelepiped, command=lambda x=parallelepiped_entry2, y=parallelepiped_entry: set_entry(x, y))
parallelepiped_button.pack(fill=X, pady=20)

parallelepiped.grid(row=1, column=3, padx=30, pady=20)

# Label
# Entry
# Frame
# Button


root.mainloop()