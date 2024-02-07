import geometries.parallelepiped as p
import geometries.tetrahedron as t
import geometries.sphere as s 

parallelepiped = p.Parallelepiped(3, 4, 5, "сталь")
tetrahedron = t.Tetrahedron(2, "дерево")
sphere = s.Sphere(1, "дерево")

print("Объем параллелепипеда:", parallelepiped.calculate_volume())
print("Площадь поверхности параллелепипеда:", parallelepiped.calculate_surface_area())
print("", parallelepiped.calculate_mass())

print("", tetrahedron.calculate_volume())
print("", tetrahedron.calculate_surface_area())
print("", tetrahedron.calculate_mass())

print("", sphere.calculate_volume())
print("", sphere.calculate_surface_area())
print("", sphere.calculate_mass())