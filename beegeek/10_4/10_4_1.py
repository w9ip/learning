s1 = input()
s2 = input()
if len(s1) == len(s2):
    print('YES' if s1 == ''.join(e for e in s1 if e in s2 and s1.count(e) == s2.count(e)) else 'NO')
else:
    print('NO')
