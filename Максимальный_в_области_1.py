n = int(input())
max_ = []
for i in range(n):
    row = [int(e) for e in input().split()][:i + 1]
    max_.append(max(row))
print(max(max_))
