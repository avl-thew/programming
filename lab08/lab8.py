# from datetime import datetime
# from time import sleep
# import functools
# from typing import Callable, Any
 
 
# def logging(func: Callable) -> Callable:
#     """Декоратор. Логирует ошибки функций с указанием даты и времени возникновения."""
 
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs) -> Any:
#         try:
#             print(f'{func.__name__}\n{func.__doc__}')
#             function = func(*args, **kwargs)
#             return function
#         except Exception as exc:
#             string = '{} - {}:\t{}\n'.format(datetime.now(), func.__name__, exc)
#             with open('function_errors.log', 'a', encoding='utf-8') as log:
#                 log.write(string)
 
#     return wrapped_func
 
 
# @logging
# def division_by_zero():
#     """Деление на нуль."""
#     sleep(1)
#     raise ZeroDivisionError('Деление на ноль')
 
 
# @logging
# def value_error():
#     """Вызывает ValueError."""
#     sleep(1)
#     raise ValueError('Неверное значение')
 
 
# @logging
# def name_error():
#     """Вызывает NameError."""
#     sleep(1)
#     raise NameError('Неверное имя')
 
 
# @logging
# def index_error():
#     """Вызывает IndexError."""
#     sleep(1)
#     raise IndexError('Нет такого индекса')
 
 
# division_by_zero()
# value_error()
# name_error()
# index_error()

#########

from typing import Callable, Any 
import functools 
import datetime 
 
 
def logging(func: Callable) -> Callable: 
    """ 
    Декоратор, логирующий функции. 
    Если во время выполнения декорируемой функции возникла ошибка, 
    то в файл function_errors.log записываются название функции и ошибки. 
    """ 
 
    @functools.wraps(func) 
    def wrapped_func(*args, **kwargs) -> Any: 
        print(f'\nНазвание функции: {func.__name__}.' 
              f'\nДокументация:{func.__doc__}') 
 
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
 
        try: 
            result = func(*args, **kwargs) 
            return result 
        except Exception as e: 
            with open('function_errors.log', 'a+', encoding='utf-8') as f: 
                f.write(f'{now} Название функции: [{func.__name__}]. ' 
                        f'Исключение: [{type(e).__name__}]. Ошибка: [{e}]\n') 
 
    return wrapped_func 
 
 
@logging 
def first_func() -> int: 
    """ Функция запрашивает ввод целочисленного числа. """ 
    number_int = int(input('Введите число: ')) 
    return number_int 
 
 
@logging 
def second_func() -> int: 
    """ Функция выводит результат деления 10 на введенное пользователем число. """ 
    number_int = int(input('Введите число: ')) 
    result = 10 // number_int 
    return result 
 
 
@logging 
def third_func() -> None: 
    """ Функция выводит текст сообщения. """ 
    print('Hello, World!') 
 
 
first_func() 
second_func() 
third_func()