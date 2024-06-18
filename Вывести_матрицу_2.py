n, m = int(input()), int(input())
lst = []
for i in range(n):
    lst.append([])
    for j in range(m):
        s = input()
        print(s, end=' ')
        lst[-1].append(s)
    print()
print()
for i in range(m):
    for j in range(n):
        print(lst[j][i], end=' ')
    print()
