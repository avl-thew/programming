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

def test_unp():
    l = [None, [1, [], ({2, 3}, {'foo': 'bar', 'a': 1})]]
    expected_result = [None, 1, 2, 3, 'foo', 'bar', 'a', 1]
    assert unp(l) == expected_result
    enp_l = [[]]
    assert unp(enp_l) == []
    
