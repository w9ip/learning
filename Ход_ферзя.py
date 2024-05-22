row1 = int(input())
col1 = int(input())

row2 = int(input())
col2 = int(input())

if row1 == row2 or col1 == col2 or (row1 - row2 == col1 - col2 or row1 - row2 == col2 - col1):
    print('YES')
else:
    print('NO')
