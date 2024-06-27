n = int(input())

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            print(1, end=' ')
        elif i > n - 1 - j:
            print(2, end=' ')
        elif i < n - 1 - j:
            print(0, end=' ')
    print()
