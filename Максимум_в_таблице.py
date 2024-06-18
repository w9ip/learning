n, m = int(input()), int(input())
max_i, max_j = 0, 0
matrix = [[int(e) for e in input().split()] for e in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[max_i][max_j]:
            max_i, max_j = i, j
print(max_i, max_j)
