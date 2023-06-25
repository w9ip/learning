N, M = map(int, input().split())
res = range(1, N*M+1)
i = 0
while i != N * M:
    print(*[str(e).ljust(2, ' ') for e in res[i:i+M]])
    i += M
