n = int(input())
mtx = []
for i in range(n):
    mtx.append([int(e) for e in input().split()])

mtx = list(zip(*mtx))
for i in range(n):
    for j in range(n):
        print(mtx[i][j], end=' ')
    print()