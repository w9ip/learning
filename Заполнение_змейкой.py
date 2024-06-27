n, m = [int(e) for e in input().split()]

matrix = [[0 for _ in range(m)] for j in range(n)]
c = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = c
        c += 1
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])
