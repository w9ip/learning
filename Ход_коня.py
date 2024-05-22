row1 = int(input())
col1 = int(input())

row2 = int(input())
col2 = int(input())

if row1 < row2:
    row1, row2 = row2, row1

if col1 < col2:
    col1, col2 = col2, col1

print('YES' if (row1 - row2) * (col1 - col2) == 2 else 'NO')
