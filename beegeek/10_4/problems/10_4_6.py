s = input()
sifr = {}
for i in s:
    sifr[i] = sifr.get(i, 0) + 1
n = int(input())
d = {}
for _ in range(n):
    inp = input().split(':')
    d[inp[0]] = int(inp[1][1:])
for i in s:
    x = sifr[i]
    for j in d:
        if x == d[j]:
            print(j, end='')
