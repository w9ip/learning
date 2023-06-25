N = range(int(input()))

M = [[0 for row in N]
     for col in N]

for i in N:
    M[i][len(N)-i-1] = 1
    M[i][i] = 1
    print(*M[i])