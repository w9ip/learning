n = int(input())
mtx = []

for i in range(n):
    mtx.append([int(e) for e in input().split()])
lst = []
for i in range(n):
    for j in range(n):
        if i + j + 1 >= n:
            lst.append(mtx[i][j])
print(max(lst))

