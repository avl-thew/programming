
# from typing import Callable, Any 
# import functools 
# import datetime 
 
# def logging(func: Callable) -> Callable: 
#     """ 
#     Декоратор, логирующий функции. 
#     Если во время выполнения декорируемой функции возникла ошибка, 
#     то в файл function_errors.log записываются название функции и ошибки. 
#     """ 
 
#     @functools.wraps(func) 
#     def wrapped_func(*args, **kwargs) -> Any: 
#         print(f'\nНазвание функции: {func.__name__}.' 
#               f'\nДокументация:{func.__doc__}') 
 
#         now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
 
#         try: 
#             result = func(*args, **kwargs) 
#             return result 
#         except Exception as e: 
#             with open('function_errors.log', 'a+', encoding='utf-8') as f: 
#                 f.write(f'{now} Название функции: [{func.__name__}]. ' 
#                         f'Исключение: [{type(e).__name__}]. Ошибка: [{e}]\n') 
 
#     return wrapped_func 

# @logging 
# def first_func() -> int: 
#     """ Функция запрашивает ввод целочисленного числа. """ 
#     number_int = int(input('Введите число: ')) 
#     return number_int 
 
 
# @logging 
# def second_func() -> int: 
#     """ Функция выводит результат деления 10 на введенное пользователем число. """ 
#     number_int = int(input('Введите число: ')) 
#     result = 10 // number_int 
#     return result 
 
 
@logging 
def third_func() -> None: 
    """ Функция выводит текст сообщения. """ 
    print('Hello, World!') 
 
 
first_func() 
second_func() 
third_func()