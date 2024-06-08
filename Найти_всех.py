def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return lst


print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))
