n = int(input())
d = {}
for _ in range(n):
    v, k = input().lower().split()
    d.setdefault(k, []).append(v)
m_keys = [input().lower() for k in range(int(input()))]
for k in m_keys:
    print(*d.get(k, ['абонент не найден']))
