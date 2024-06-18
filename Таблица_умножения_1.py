n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
        print(str(mult[i][j]).ljust(2), end=' ')
    print()
