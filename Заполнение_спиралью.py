def create_spiral_matrix(n, m):
    # Инициализация пустой матрицы
    matrix = [[0] * m for _ in range(n)]

    # Начальные значения
    num = 1
    row, col = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Вправо, вниз, влево, вверх
    direction_index = 0

    while num <= n * m:
        # Заполняем текущую ячейку
        matrix[row][col] = num
        num += 1

        # Рассчитываем следующую ячейку
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]

        # Проверка выхода за границы или на заполненную ячейку
        if (0 <= next_row < n and 0 <= next_col < m and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            # Меняем направление
            direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]

    # Печать матрицы
    for row in matrix:
        print(" ".join(str(x).ljust(3) for x in row))


# Чтение ввода
n, m = map(int, input().split())

# Создание и вывод матрицы
create_spiral_matrix(n, m)
