# test_prime.py

import pytest
from lab9 import prime_num

def test_prime():
    gen = prime_num()
    primes = []

    for i in range(100):
        p = next(gen)
        primes.append(p)

        for j in range(2, int(p**0.5) + 1):
            assert p % j != 0
    
    assert len(primes) == 100
    


# В этом тесте:
# 1.Создается генератор prime_num()
# 2.Генерируется первые 100 простых чисел
# 3.Для каждого числа проверяется, что оно не делится на числа от 2 до квадратного корня из этого числа
# 4.Проверяется, что было сгенерировано ровно 100 простых чисел

# Чтобы запустить тест:
# Сохранить тест в файл test_prime.pyВыполнить в терминале:
# pytest test_prime.py