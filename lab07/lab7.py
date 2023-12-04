# >>> unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
# [None, 1, 2, 3, 'foo', 'bar']

def  packet(n):
    n = unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
    return n


# def func(i):
#     if i == 1:
#         print(0.3)
#         return 0.3
#     elif i == 2:
#         print(- 1.5)
#         return - 1.5
#     else:
#         A = (func(i-1) * func(i-2)) * ((i-1)**2)/((i+1)**3)
#         print(A)
#         return A

# func(1)
