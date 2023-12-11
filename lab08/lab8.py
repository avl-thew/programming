


# замыкание
def fread(filename: str):
    file = open(filename, "r")
    def read():
        return file.readline()
    return read
get_line = fread("text.txt")
print(get_line())

# декоратор
def logger(filename):
    my_file = open('py_log.log', 'w+')
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            my_file.write(f"Вызов функции {func} с аргументами {args}, {kwargs}"'\n')
            result = func(*args, **kwargs)

            my_file.write(f"Функция {func} вернула результат: {result}")
            return result
        return wrapper
    return my_decorator
@logger('my_file')
def mult(num1, num2):
    return num1 * num2
print(mult(4,7))





################# замыкание через декоратор

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func} с аргументами {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Функция {func} вернула результат: {result}")
#         return result
#     return wrapper

# def fread(filename: str):
#     file = open(filename, "r")
#     @logger(('py_log.log', 'w+'))
#     def read():
#         return file.readline()
#     return read

# get_line = fread("text.txt")
# print(get_line())