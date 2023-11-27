inp_n = int(input())
d = {}
for _ in range(inp_n):
    inp = input().split()
    k = tuple(inp[1:])
    v = inp[0]
    d[k] = v

print(*[d[tuple(e for e in d.keys() if k in e)[0]] for k in [input() for _ in range(int(input()))]], sep='\n')
