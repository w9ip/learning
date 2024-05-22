n = int(input())

a = n % 10
b = (n % 100) // 10
c = n // 100

_max = max(a, b, c)
_min = min(a, b, c)

s = (a + b + c) - _max - _min

if _max - _min == s:
    print('Число интересное')
else:
    print('Число неинтересное')
