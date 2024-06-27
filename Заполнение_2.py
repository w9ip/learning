n, m = [int(e) for e in input().split()]
for i in range(n):
    for j in range(m):
        print(str(i + j * n + 1).ljust(3), end='')
    print()
