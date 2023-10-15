n = int(input())
mtx = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        mtx[i][j] = abs(i - j)
        print(mtx[i][j], end=' ')
    print()
