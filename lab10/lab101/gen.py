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

# gen = prime_num()
# values = []

# for _ in range(5):
#     values.append(next(gen))