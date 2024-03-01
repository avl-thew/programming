from distance import distance
from logic04 import Family
from circle import Logic

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