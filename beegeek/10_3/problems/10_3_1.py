dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

dict3 = dict1 | dict2

for k in dict3:
    if (k in dict1) and (k in dict2):
        result[k] = dict1[k] + dict2[k]
    else:
        result[k] = dict1[k] if k in dict1 else dict2[k]
