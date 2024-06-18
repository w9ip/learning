n = int(input())
matrix = []
max_list = []
for i in range(n):
    row = [int(e) for e in input().split()]
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if i == j:
            max_list.append(matrix[i][j])
        if j < i < n - 1 - j:
            max_list.append(matrix[i][j])
        if j > i > n - 1 - j:
            max_list.append(matrix[i][j])
        if i + j + 1 == n:
            max_list.append(matrix[i][j])
print(max(max_list))
