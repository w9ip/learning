n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n or i == 0 or i + 1 == n or (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
            print(str(1).ljust(3), end='')
        else:
            print(str(0).ljust(3), end='')
    print()
