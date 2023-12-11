# >>> unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
# [None, 1, 2, 3, 'foo', 'bar']

l = [None, [1, [], ({2, 3}, {'foo': 'bar', 'a': 1})]]

def unp(l):
    result = []
    for item in l:
        if not item:
             result.append(None)
        if not item:
            result.append((unp(item)))
        # if isinstance(item, ()):
        #     result.extend(unp())
        elif isinstance(item, (int, str)):
            result.append(item)
        elif isinstance(item, (list, tuple, set)):
            result.extend((unp(item)))
        elif isinstance(item, dict):
            result.extend(unp(item.items()))
    return result

print(unp(l))




def func(i):
    if i == 1:
        return 0.3
    elif i == 2:
        return -1.5
    else:
        A = (func(i-1) * func(i-2)) * ((i-1)**2)/((i+1)**3)
        return A
print(func(5))
