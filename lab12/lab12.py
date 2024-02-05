import packege.parallelepiped as p
import packege.tetrahedron as t
import packege.sphere as s 

 parallelepiped = p.Parallelepiped(3, 4, 5, "сталь")
 tetrahedron = t.Tetrahedron(2, "дерево")
 sphere = s.Sphere(1, "дерево")

 print("Объем параллелепипеда:", parallelepiped.calculate_volume())
 print("Площадь поверхности параллелепипеда:")
 print()