n = int(input())  # n & 1 == True

for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
