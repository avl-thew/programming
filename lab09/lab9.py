def is_prime(n):
    if n<=3:
        return True
    if n%2==0:
        return False
    k=3
    while k*k<=n:
        if n%k==0:
            return False
        k+=2
    return True
    
    
def gprimes(last):
    c=1
    while True:
        if c>last:
            return
        if is_prime(c):
            yield c
        c+=1    
 
primes=list(gprimes(100))
print(primes)


def prime_generator(x):
    prs = {}
    p = 1
    while p < x:
        if p not in prs:
            yield p
            prs[p * p] = [p]
        else:
            for s in prs[p]:
                prs.setdefault(s + p, []).append(s)
            del prs[p]
 
        p += 1
print(prime_generator)