import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from docx import Document
from openpyxl import Workbook
from parallelepiped import Parallelepiped
from tetrahedron import Tetrahedron
from sphere import Sphere

# import docx
# import openpyxl

def save_to_doc(result):
        doc = Document()
        doc.add_paragraph(f'Результат: {result}')
        doc.save('результат.docx')

def save_to_xls(result):
        wb = Workbook()
        ws = wb.active
        ws['A1'] = 'Результат:'
        ws['B1'] = result
        wb.save('результат.xlsx')

# Словарь с плотностями разных материалов
densities = {'Дерево': 500, 'Металл': 7800, 'Пластик': 1300}

# Функция для открытия окна ввода параметров    
def open_input_window(root, shape, density):
    input_window = tk.Toplevel(root)
    root.withdraw()
    
    if shape == 'Параллелепипед':
        a_label = tk.Label(input_window, text='Сторона a:')
        a_entry = tk.Entry(input_window)
        b_label = tk.Label(input_window, text='Сторона b:')
        b_entry = tk.Entry(input_window)
        c_label = tk.Label(input_window, text='Сторона c:')
        c_entry = tk.Entry(input_window)
        
        a_label.grid(row=0, column=0)
        a_entry.grid(row=0, column=1)
        b_label.grid(row=1, column=0)
        b_entry.grid(row=1, column=1)
        c_label.grid(row=2, column=0)
        c_entry.grid(row=2, column=1)
        
        def calculate():
            a = float(a_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            p = Parallelepiped()
            V, S, m = p.calculate_parallelepiped(a, b, c, density)
            input_window.withdraw()
            open_result_window(root, V, S, m)
            
        calc_button = tk.Button(input_window, text='Рассчитать', command=calculate)
        calc_button.grid(row=3, column=0, columnspan=2)
        
    elif shape == 'Тетраэдр':
        a_label = tk.Label(input_window, text='Ребро a:')
        a_entry = tk.Entry(input_window)
        
        a_label.grid(row=0, column=0)
        a_entry.grid(row=0, column=1)
        
        def calculate():
            a = float(a_entry.get())
            t = Tetrahedron()
            V, S, m = t.calculate_tetrahedron(a, density)
            input_window.withdraw()
            open_result_window(root, V, S, m)
            
        calc_button = tk.Button(input_window, text='Рассчитать', command=calculate)
        calc_button.grid(row=1, column=0, columnspan=2)
        
    else:
        R_label = tk.Label(input_window, text='Радиус R:')
        R_entry = tk.Entry(input_window)
        
        R_label.grid(row=0, column=0)
        R_entry.grid(row=0, column=1)
        
        def calculate():
            R = float(R_entry.get())
            s = Sphere()
            V, S, m = s.calculate_sphere(R, density)
            input_window.withdraw()
            open_result_window(root, V, S, m)
            
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

  ok_button = tk.Button(result_window, text='ОК', command=root.destroy)
  ok_button.grid(row=3, column=0)
  
  def open_result_window(root, V, S, m):
    def ok_button_clicked():
        V = V
        S = S 
        m = m
        save_to_doc(V)
        save_to_xls(S) 
        open_result_window(root, V, S, m)
        root.destroy()   

    ok_button = tk.Button(result_window, text='ОК', command=ok_button_clicked)

def main():
  root = tk.Tk()
  root.title('Плотность')
  root.geometry('300x200')
  
  shape_label = tk.Label(root, text='Выберите фигуру:')
  shape_label.pack()

  shape = tk.StringVar()
  shape.set('Параллелепипед')

  material = tk.StringVar()
  material.set('Дерево')
  
  material_dropdown = ttk.Combobox(root, textvariable=material, values=list(densities.keys()), state='readonly')
  material_dropdown.pack()  

  parallelepiped_radio = tk.Radiobutton(root, text='Параллелепипед', variable=shape, value='Параллелепипед')
  parallelepiped_radio.pack()

  tetrahedron_radio = tk.Radiobutton(root, text='Тетраэдр', variable=shape, value='Тетраэдр')
  tetrahedron_radio.pack()  

  sphere_radio = tk.Radiobutton(root, text='Шар', variable=shape, value='Шар')
  sphere_radio.pack()

  custom_density_label = tk.Label(root, text="Плотность материала:")
  custom_density_entry = tk.Entry(root)

  custom_density_label.pack()
  custom_density_entry.pack()
  
  custom_density = custom_density_entry.get()
  if len(custom_density) > 0:
    density = float(custom_density)
  else:
    density = densities[material.get()]
  
  input_button = tk.Button(root, text='Ввести параметры', command=lambda: open_input_window(root, shape.get(), density))
  input_button.pack()  
  
  root.mainloop()

if __name__ == '__main__':
    main()
