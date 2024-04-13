
# вычислить интеграл
# import sympy
# from sympy.abc import x

# f = 1/(x*((x+1)**2))
# print(sympy.integrate(f, (x, 1, 2)))


# вычислить интегральную сумму
import sympy as sp

a = 1
b = 2 
n = 7

x = sp.Symbol('x')
f = 1/(x*(x+1)**2)

h = (b - a) / n
result = 0
for i in range(n):
    xk = a + h/2 + i*h
    result += f.subs(x, xk)
    
result *= h

print(result)
