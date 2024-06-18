n, m = int(input()), int(input())
matrix = [[int(e) for e in input().split()] for _ in range(n)]
c1, c2 = [int(e) for e in input().split()]
for i in range(n):
    matrix[i][c1], matrix[i][c2] = matrix[i][c2], matrix[i][c1]
    print(*matrix[i])
