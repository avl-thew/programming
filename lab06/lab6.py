#1 

import itertools
alp = "АНДРЕЙ"
ar = itertools.product(alp, repeat=6) 
arl = []
for i in ar:
    arl.append(list(i))
flag = True
count = 0
for e in arl:
    if e.count('Й') > 1 or e[0] == 'Й' or e[-1] == 'Й' :
        
        for i in range(len(e)-1):
            if (e[i] == 'Й' and e[i + 1] == 'Е') or (e[i + 1] == 'Й' and e[i] == 'Е'):
                flag = False
        if flag == True: count += 1
print(count)



# k=0
# for x1 in 'андрей':
#     for x2 in 'андрей':
#         for x3 in 'андрей':
#             for x4 in 'андрей':
#                 for x5 in 'андрей':
#                     for x6 in 'андрей':
#                         s=x1+x2+x3+x4+x5+x6
#                         if s.count('й')<=1 and x1!='й' and x6!='й' and s.count('ей')==0 and s.count('йе')==0:
#                             k=k+1   
# print(k)



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
    
       





