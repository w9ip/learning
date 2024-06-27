n, m = [int(e) for e in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
tmp = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                tmp += 1
                matrix[i][j] = tmp
for i in matrix:
    print(*i)
