# https://stepik.org/lesson/416757/step/6?unit=406265

N = int(input())

M = [[0 for row in range(N)] for col in range(N)]

for i in range(len(M)):
    for j in range(len(M)):
        if i < j and i < N - 1 - j:
            M[i][j] = 1
        if i > j and i > N - 1 - j:
            M[i][j] = 1
    M[i][N-i-1] = 1
    M[i][i] = 1
    print(*M[i])