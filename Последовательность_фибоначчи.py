n = int(input())
f1 = f2 = 1
print(f2, end=' ')
for i in range(0, n-1):
    print(f2, end=' ')
    f1, f2 = f2, f2 + f1
