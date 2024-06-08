s = input().split()

for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)
