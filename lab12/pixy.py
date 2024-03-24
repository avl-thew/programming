import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mb
from parallelepiped import Parallelepiped
from tetrahedron import Tetrahedron
from sphere import Sphere



def open_input_window(root, shape):
    input_window = tk.Toplevel(root)
    root.withdraw()
    
    if shape == 'Параллелепипед':
        a_label = tk.Label(input_window, text='Длина:')
        a_entry = tk.Entry(input_window)
        b_label = tk.Label(input_window, text='Ширина:')
        b_entry = tk.Entry(input_window)
        c_label = tk.Label(input_window, text='Высота:')
        c_entry = tk.Entry(input_window)
        density_entry = tk.Label(input_window, text='Плотность:')
        density_entry = tk.Entry(input_window)
        
        a_label.grid(row=0, column=0)
        a_entry.grid(row=0, column=1)
        b_label.grid(row=1, column=0)
        b_entry.grid(row=1, column=1)
        c_label.grid(row=2, column=0)
        c_entry.grid(row=2, column=1)
        density_entry.grid(row=3, column=0)
        density_entry.grid(row=3, column=1)
        
            
        def calculate(self):
            a = float(a_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            density = float(density.get())
            p = Parallelepiped()
            V, S, m = p.calculate_parallelepiped(self.selected_shape, a, b, c, density)
            input_window.withdraw()
            open_result_window(root, V, S, m)
                
        calc_button = tk.Button(input_window, text='Рассчитать', command=calculate)
        calc_button.grid(row=3, column=0, columnspan=2)
        
    elif shape == 'Тетраэдр':
        a_label = tk.Label(input_window, text='Длина:')
        a_entry = tk.Entry(input_window)
        density_entry = tk.Label(input_window, text='Плотность:')
        density_entry = tk.Entry(input_window)    
        a_label.grid(row=0, column=0)
        a_entry.grid(row=0, column=1)
        density_entry.grid(row=1, column=0)
        density_entry.grid(row=1, column=1)
            
        def calculate(self):
            a = float(a_entry.get())
            density = float(density.get())
            t = Tetrahedron()
            V, S, m = t.calculate_tetrahedron(self.selected_shape, a, density)
            input_window.withdraw()
            open_result_window(root, V, S, m)
                
        calc_button = tk.Button(input_window, text='Рассчитать', command=calculate)
        calc_button.grid(row=1, column=0, columnspan=2)
        
    else:
        R_label = tk.Label(input_window, text='Радиус R:')
        R_entry = tk.Entry(input_window)
        density_entry = tk.Label(input_window, text='Плотность:')
        density_entry = tk.Entry(input_window)    
        R_label.grid(row=0, column=0)
        R_entry.grid(row=0, column=1)
        density_entry.grid(row=1, column=0)
        density_entry.grid(row=1, column=1)
        
        def calculate(self):
            R = float(R_entry.get())
            density = float(density.get())
            s = Sphere()
            V, S, m = s.calculate_sphere(self.selected_shape, R, density)
                
            input_window.withdraw()
            open_result_window(root, V, S, m)
            
        density_label = tk.Label(input_window, text='Плотность:')
        density_entry = tk.Entry(input_window)

        density_label.grid(row=3, column=0) 
        density_entry.grid(row=3, column=1)
    
        calc_button = tk.Button(input_window, text='Рассчитать', command=calculate)
        calc_button.grid(row=1, column=0, columnspan=2)

def open_result_window(root, V, S, m):
    result_window = tk.Toplevel(root)
    
    V_label = tk.Label(result_window, text=f'Объем (V): {V:.2f}')
    S_label = tk.Label(result_window, text=f'Площадь (S): {S:.2f}') 
    m_label = tk.Label(result_window, text=f'Масса (m): {m:.2f}')

    V_label.grid(row=0, column=0)
    S_label.grid(row=1, column=0)
    m_label.grid(row=2, column=0)

    ok_button = tk.Button(result_window, text='ОК', command=lambda: [root.destroy(), result_window.destroy()])

    ok_button.grid(row=3, column=0)



class MainGUI:
    
  def __init__(self, root):
      self.root = root
    
      self.root.title("LAB 12") 
      self.root.geometry('400x300')
      self.label = tk.Label(self.root, text='Выберите фигуру:')
      self.label.pack()
      
      self.shape_var = tk.StringVar()
      self.selected_shape = tk.StringVar()
      self.shape_radio1 = tk.Radiobutton(self.root, text="Параллелепипед", variable=self.shape_var, value="parallelepiped")
      self.shape_radio1.pack()

      self.shape_radio2 = tk.Radiobutton(self.root, text="Тетраэдр", variable=self.shape_var, value="tetrahedron")
      self.shape_radio2.pack()

      self.shape_radio3 = tk.Radiobutton(self.root, text="Шар", variable=self.shape_var, value="sphere")
      self.shape_radio3.pack()
      
      selected_shape = self.selected_shape.get()
      if self.selected_shape == "parallelepiped":
         self.show_parallelepiped_input()
      elif selected_shape == "tetrahedron":  
        self.show_tetrahedron_input()
      if selected_shape == "sphere":
        self.show_sphere_input()
      
      self.input_button = tk.Button(self.root, text='Ввести параметры', command=lambda: open_input_window(self.root, self.shape_var.get()))
      self.input_button.pack()  
  

  def run(self):
    self.root.mainloop()
    
if __name__ == '__main__':
  root = tk.Tk()
  gui = MainGUI(root)
  gui.run()
  
  
