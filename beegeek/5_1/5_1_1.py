strs = input().split()
n = int(input())
mtx = [[] for _ in range(n)]

i = 0
c = 0
while i < len(strs):
    mtx[c].append(strs[i])
    c += 1
    if c == n:
        c = 0
    i += 1

print(mtx)