l = input().split()
m = input().split()
print(*[int(m[i]) + int(l[i]) for i in range(len(l))])
