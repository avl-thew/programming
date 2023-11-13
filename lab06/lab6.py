import itertools
alp = "АНДРЕЙ"
ar = itertools.product(alp, repeat=6) 
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    f = True
    for i in range(len(e) - 1):
        if e.count('Й') > 1 or e[0] == 'Й' or e[-1] == 'Й' or (e[i] == 'Й' and e[i + 1] == 'Е') or (e[i + 1] == 'Й' and e[i] == 'Е'):
            f = False
    if f == True: count += 1
print(count)



n = 8**2020 + 4*2017 + 26 - 1
s = bin(n)[2:]
print(s.count('1'))




def f(n):
    b = set()
    for d in range (2, int(n**0.5) + 1):
        if n%d == 0:
            b.add(d)
            b.add(n//d)
            break
    return b

m = 0
for n in range(245690 , 245756 + 1):
    m +=1
    k = f(n)
    if len(k) == 0:
        print(n, m)
       