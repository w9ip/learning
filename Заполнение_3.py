n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            print(str(1).ljust(3), end='')
        else:
            print(str(0).ljust(3), end='')
    print()
