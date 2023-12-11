


# замыкание
def fread(filename: str):
    file = open(filename, "r")
    def read():
        return file.readline()
    return read
get_line = fread("text.txt")
print(get_line())

# декоратор
def my_decorator(*args):
    def logger(func):
        def wrapper(*args, **kwargs):
            print(f"Вызов функции {func} с аргументами {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"Функция {func} вернула результат: {result}")
            return result
        return wrapper
    return logger
# my_file = open(('py_log.log'))
    @logger
    # (open('py_log.log', 'w+'))
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