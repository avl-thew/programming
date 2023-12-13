def logger(filename):
    my_file = open(filename, 'w+')
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


@logger('nup.log')
def fread(filename: str):
    file = open(filename, "r")
    def read():
        return file.readline()
    return read