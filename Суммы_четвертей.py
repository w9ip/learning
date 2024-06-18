n = int(input())
matrix = []
first, second, third, fourth = [], [], [], []
for i in range(n):
    row = [int(e) for e in input().split()]
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            fourth.append(matrix[i][j])
        if j > i > n - 1 - j:
            second.append(matrix[i][j])
        if i > j and i > n - 1 - j:
            third.append(matrix[i][j])
        if i < j and i < n - 1 - j:
            first.append(matrix[i][j])

print('Верхняя четверть:', sum(first))
print('Правая четверть:', sum(second))
print('Нижняя четверть:', sum(third))
print('Левая четверть:', sum(fourth))
