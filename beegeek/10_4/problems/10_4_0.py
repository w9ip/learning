n = int(input())
d = {}
for _ in range(n):
    kv = input().split(':')
    d[kv[0].lower()] = kv[1][1:]
m = int(input())
for _ in range(m):
    res = d.get(input().lower(), 'Не найдено')
    print(res)
