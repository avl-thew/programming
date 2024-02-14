
# декоратор
def logger(filename = "nup.log1"):
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


@logger()
def fread(filename: str):
    file = open(filename, "r")
    def read():
        return file.readline()
    return read


if __name__=="__main__":
    get_line = fread("text.txt")
    print(get_line())
    print(get_line())
    print(get_line())

l = [None, [1, [], ({2, 3}, {'foo': 'bar', 'a': 1})]]
@logger()
def unp(l):
    result = []
    for item in l:
        if item is None:
             result.append(None)
        elif isinstance(item, (int, str)):   
            result.append(item)
        elif isinstance(item, (list, tuple, set)):
            if item:
                result.extend((unp(item)))    
        elif isinstance(item, dict):
            if item:
                result.extend(unp(item.items()))
        else:
            result.append(item)
    return result

unp(l)
