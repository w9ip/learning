s1, s2, s3 = len(input()), len(input()), len(input())

_min = min(s1, s2, s3)
_max = max(s1, s2, s3)
d = (s1 + s2 + s3) - (_min + _max)
if (_max - d) == (d - _min):
    print('YES')
else:
    print('NO')


a, b, c = len(input()), len(input()), len(input())
if a + b + c == (min(a, b, c) + max(a, b, c))/2*3:
    print("YES")
else:
    print("NO")