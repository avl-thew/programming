# Лабораторная работа №4
## Задание 
```
Напишите верхнеуровневый модуль, который будет использовать логику из модулей-заданий. Перед этим нужно будет придумать способ инкапсулировать логику для корректного импортирования.
```
логика написана только для файла 00_distance, 01_circle, 04_my_family, 10_store.
для остальных логика была либо слишком трививальной, либо ее не было.



### distance.py
```Python
def distance(a: tuple, b: tuple) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
```

### circle.py

```Python
class Logic:
    def __init__(self):
        self.pi = 3.1415926
        self.r = 42
        self.S = self.pi * self.r ** 2
    
    def calculate_area(self):
        return self.S
```


### logic04

```Python
class Family:
    def __init__(self, member_names, member_heights):
        self.members = member_names
        self.heights = member_heights
    
    def get_member_height(self, member_name):
        # Ищем соответствующую высоту члена семьи
        index = self.members.index(member_name)
        height = self.heights[index]
        return height
    
    def get_total_height(self):
        # Суммируем все значения в списке heights
        total_height = sum(self.heights)
        return total_height
```

### store
```Python
GOODS = {
  'Лампа': '12345',
  'Стол': '23456',
  'Диван': '34567',
  'Стул': '45678',
}

STORE = {
  '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
def get_goods():
  return GOODS

def get_store_data():
  return STORE

def calculate_item_cost(item_code):
  item_data = STORE[item_code]
  
  total_quantity = 0
  total_cost = 0
  
  for item in item_data:
    total_quantity += item['quantity']
    total_cost += item['quantity'] * item['price']

chair_cost = chair_quantity * chair_price + chair_quantity1 * chair_price1 + chair_quantity2 * chair_price2

print('Стул -', chair_quantity+chair_quantity1+chair_quantity2, 'шт, стоимость', chair_cost, 'руб')
```

### верхнеуровневый модуль запускается в файле main.py

```Python
from distance import distance
from logic04 import Family
from circle import Logic
from store import get_goods, calculate_item_cost

goods = get_goods()
calculate_item_cost(goods['Лампа'])

a = 550
b = 600
print()


# Создаем экземпляр класса Family
my_family = Family(['Mother', 'Father', 'I'], [160, 187, 172])

# Получаем и выводим высоту члена семьи 'Father'
father_height = my_family.get_member_height('Father')
print('Рост отца:', father_height)

# Вычисляем и выводим общую сумму всех высот в семье
total_height = my_family.get_total_height()
print('Общий рост семьи:', total_height)


logic = Logic()
print(logic.calculate_area())
```
![alt text](<Снимок экрана 2024-03-10 203849.png>)