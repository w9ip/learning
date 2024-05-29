n = int(input())
lst = []
for i in range(n):
    lst.append(input())
k = int(input())
for element in lst:
    if len(element) < k:
        continue
    print(element[k - 1], end='')
