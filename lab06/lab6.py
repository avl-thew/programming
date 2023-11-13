#1 
import itertools
alp = "АНДРЕЙ"
ar = itertools.product(alp, repeat=6) 
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
print(count)

#2
n = 8**2020 + 4**2017 + 26 - 1
s = bin(n)[2:]
print(s.count('1'))

#3 
def f(n):
    for d in range (2, int(n**0.5) + 1):
        if n%d == 0:
            return False
    return True

m = 0
for n in range(245690 , 245756 + 1):  
    m += 1
    if f(n) == True:
        print(m, n)
    
       





