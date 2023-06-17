# https://stepik.org/lesson/416757/step/2?unit=406265


N = range(int(input()))

M = [[row for row in N]
     for col in N]

for i in range(len(M)):
    X = M[i][len(M) - 1 - i]
    for k in M[i]:
        if k != X and k < X:
            M[i][k] = 0
        else:
            M[i][k] = 2
    M[i][len(M) - 1 - i] = 1
    print(*M[i])
