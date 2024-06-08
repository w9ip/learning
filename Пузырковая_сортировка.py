a = [5, 1, 8, 2, 4]
n = len(a)
for i in range(n - 1):
    flag = False
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print('Сортированный массив:', a)
