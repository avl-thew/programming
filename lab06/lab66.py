import itertools
import doctest
def F(alp,b):
    """
    Составляет комбинацию по заданному условию
    :param alp: алфавит для комбинаций
    :param b: количчество символов в 1 комбинации
    :return: количество комбинаций

    >>> F("АНДРЕЙ",6)
    23625
    """
    ar = itertools.product(alp, repeat=b)
    arl = []
    for i in ar:
        arl.append(''.join(i))

    count = 0
    for e in arl:
        e[0] == 'Й'
        e[-1] == 'Й'
        if e.count('Й') > 1:
            continue
        if  e.startswith('Й'):
            continue
        if  e.endswith('Й'):
            continue
        flag = True
        for i in range(len(e)-1):
            if (e[i] == 'Й' and e[i + 1] == 'Е') or (e[i + 1] == 'Й' and e[i] == 'Е'):
                flag = False
                break
        if flag == True: count += 1
    return count

print(F("АНДРЕЙ",6))

if __name__ == '__main__':
    doctest.testmod(name='F', verbose=True)


import doctest
def F(a):
    """
    Подсчет количества единиц в двоичной записи числа
    :param a: число в десятичной записи
    :return: количество едениц в числе

    >>> F(82020 + 42017 + 26 - 1)
    10
    """
    a_2 = bin(a)[2:]
    k = a_2.count('1')
    return k

print(F(82020 + 42017 + 26 - 1))

import doctest
def F(n):
    """
    Проверяет, является ли число n простым.

    >>> F(2)
    True
    >>> F(4)
    False
    >>> F(13)
    True
    >>> F(15)
    False
    """
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True
    m = 0
    for n in range(245690 , 245756 + 1):  
        m += 1
        if f(n) == True:
            print(m, n)

if __name__ == '__main__':
    doctest.testmod(name='F', verbose=True)