n, m = [int(e) for e in input().split()]

for i in range(n):
    for j in range(m):
        print((i + j) % m + 1, end=' ')
    print()
