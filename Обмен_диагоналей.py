matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]
md = []
pd = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            md.append(matrix[i][j])
        if i + j + 1 == len(matrix):
            pd.append(matrix[i][j])
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            matrix[i][j] = pd.pop()
        if i + j + 1 == len(matrix):
            matrix[i][j] = md.pop()
    print(*matrix[i])
