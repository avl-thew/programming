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


if __name__ == "__main__":
    a = prime_num()
    for i in a:
        print(i)
        if i > 100:
            break
