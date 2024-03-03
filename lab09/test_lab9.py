import pytest
from lab9 import prime_num

def test_prime_num():
    gen = prime_num()
    
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    
    for _ in range(10):
        next(gen)
        
    assert next(gen) == 29
    assert next(gen) == 31
    
def test_type():
    gen = prime_num()
    assert isinstance(next(gen), int)
    
def test_no_evens():
    gen = prime_num()
    for i in range(100):
        assert next(gen) % 2 != 0


# Эти тесты проверяют:

# Первые несколько простых чисел генерируются корректно
# Тип возвращаемого значения - int
# Числа не четные (т.к. простые числа не четные)