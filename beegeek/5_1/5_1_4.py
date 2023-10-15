n = int(input())
mtx = [['.' for _ in range(8)] for _ in range(8)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n or i == j or i == n // 2 or j == n // 2:
            mtx[i][j] = "*"
        print(mtx[i][j], end=' ')
    print()
