# def is_prime(n):
#     if n<=3:
#         return True
#     if n%2==0:
#         return False
#     k=3
#     while k*k<=n:
#         if n%k==0:
#             return False
#         k+=2
#     return True
    
    
# def gprimes(last):
#     c=1
#     while True:
#         if c>last:
#             return
#         if is_prime(c):
#             yield c
#         c+=1    
 
# primes=list(gprimes(100))
# #print(primes)

import math
def prime_num():
    nm = 2
    while True:
        k = math.ceil(nm ** 1 / 2)
        for i in range(2, k + 1):
            if (nm % i) == 0:
                break
        else:
            yield nm
        nm += 1

    