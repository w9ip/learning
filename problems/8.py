# N-rows
# M-columns

N, M = map(int, input().split())
pattern = [e for e in range(1, M + 1)]

for i in range(N):
    print(*pattern)
    end = pattern.pop(0)
    pattern.append(end)
