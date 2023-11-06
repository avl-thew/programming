import itertools
alphabet = "АНДРЕЙ"
ar = itertools.product(alphabet, repeat=6) #Размещение с повторениями
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    flag = True
    for i in range(len(e) - 1):
        if e.count('Й') > 1 or e[0] == 'Й' or e[-1] == 'Й' or (e[i] == 'Й' and e[i + 1] == 'Е') or (e[i + 1] == 'Й' and e[i] == 'Е'):
            flag = False
    if flag == True: count += 1
print(count)



n = 8**2020 + 4*2017 + 26 - 1
s = bin(n)[2:]
print(s.count('1'))


def prost(x):
    for n in range(1, x + 1):
        coun = 0
        if x % n == 0:
            coun += 1
        if coun >= 3:
            return False
        if n == x and coun == 2:
            return True

cou = 1

for i in range(245690, 245757):
    if prost(i):
        print(str(cou) + " " + str(i))
        cou = cou + 1