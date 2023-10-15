n = int(input())
mtx = []
for i in range(n):
    mtx.append([int(e) for e in input().split()])
# если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже - i + j + 1 > n

flag = False
for i in range(n):
    for j in range(n):
        if mtx[i][j] != mtx[n - j - 1][n - i - 1]:
            flag = True
        else:
            flag = False
print("NO" if flag else "YES")
