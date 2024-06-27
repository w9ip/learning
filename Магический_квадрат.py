matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]
n = len(matrix)
all_elem = [matrix[i][j] for i in range(n) for j in range(n)]
all_elem.sort()
md = sum(matrix[i][i] for i in range(n))
pd = sum(matrix[i][n - i - 1] for i in range(n))
cols = [sum([matrix[i][j] for i in range(n)]) for j in range(n)]
rows = [sum([matrix[j][i] for i in range(n)]) for j in range(n)]
condition1 = md == pd
condition2 = sum(all_elem) == md * n == pd * n
condition3 = cols == rows
condition4 = all_elem == list(range(1, n ** 2 + 1))
if condition1 and condition2 and condition3 and condition4:
    print('YES')
else:
    print('NO')
