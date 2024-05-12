import tkinter as tk
import  math

class Parallelepiped:

    def calculate_parallelepiped(root, a, b, c, density):
        V = a * b * c
        S = 2 * (a*b + b*c + a*c)
        m = V * density
        return V, S, m
    
    
    
    
    