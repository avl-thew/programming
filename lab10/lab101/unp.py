def unp(l):
    result = []
    for item in l:
        if item is None:
             result.append(None)
        elif isinstance(item, (int, str)):   
            result.append(item)
        elif isinstance(item, (list, tuple, set)):
            if item:
                result.extend((unp(item)))    
        elif isinstance(item, dict):
            if item:
                result.extend(unp(item.items()))
        else:
            result.append(item)
    return result


def func(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    return func(i - 1) * func(i - 2) * ((i - 1) ** 2) / ((i + 1) ** 3)