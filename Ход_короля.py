строка_1 = int(input())
столбец_1 = int(input())

строка_2 = int(input())
столбец_2 = int(input())

dif_col = столбец_1 - столбец_2
dif_row = строка_1 - строка_2

if (dif_col == 1 or dif_col == -1 or dif_col == 0) and (dif_row == 1 or dif_row == -1 or dif_row == 0):
    print('YES')
else:
    print('NO')
