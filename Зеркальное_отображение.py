matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]

# Дана квадратная матрица
# Необходимо отобразить зеркально, относительно горизонтальной оси

# [[1, 2], [2, 1]] => [[2, 1], [1, 2]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
n = len(matrix)

for i in range(n // 2):
    matrix[i], matrix[-(i+1)] = matrix[-(i+1)], matrix[i]

for row in matrix:
    print(*row)
