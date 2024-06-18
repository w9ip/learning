n = int(input())
total = 0
for i in range(n):
    total += [int(e) for e in input().split()][i]
print(total)
