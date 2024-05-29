lst = []
for _ in range(int(input())):
    lst.append(int(input()))
del lst[lst.index(max(lst))]
del lst[lst.index(min(lst))]
print(*lst, sep='\n')
