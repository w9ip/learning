ignore = ' .,!?:;-'
s1 = [e for e in input().lower() if e not in ignore]
s2 = [e for e in input().lower() if e not in ignore]
res = [
    e for e in s1
    if (e not in ignore) and (e in s2) and (s1.count(e) == s2.count(e))
]
print('YES' if s1 == res else 'NO')
