matrix = [[int(e) for e in input().split()] for e in range(int(input()))]
flag = True
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i > j and not matrix[i][j] == matrix[j][i]:
            flag = False
    if not flag:
        break
if flag:
    print('YES')
else:
    print('NO')
