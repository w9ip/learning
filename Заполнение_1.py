n, m = [int(e) for e in input().split()]
c = 1
for i in range(n):
    for j in range(m):
        print(str(c).ljust(3), end='')
        c += 1
    print()
