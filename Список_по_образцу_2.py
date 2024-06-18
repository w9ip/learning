n = int(input())
lst = []
for i in range(1, n + 1):
    lst.append([])
    for j in range(i):
        lst[i - 1].append(j + 1)
print(*lst, sep='\n')
