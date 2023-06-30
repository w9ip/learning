# N-rows
# M-columns

N, M = map(int, input().split())
gen = (e for e in range(1, N * M + 1))
matrix = []

for row in range(1, N + 1):
    matrix.append([])
    for row_elem in range(1, M + 1):
        matrix[row - 1].append(str(next(gen)).ljust(2, ' '))

for i in range(N):
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])
