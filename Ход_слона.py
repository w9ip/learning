row1 = int(input())
col1 = int(input())

row2 = int(input())
col2 = int(input())

if row1 > row2:
    if col1 > col2:
        if row1 - row2 == col1 - col2:
            print('YES')
        else:
            print('NO')
    else:
        if row1 - row2 == col2 - col1:
            print('YES')
        else:
            print('NO')
else:
    if col1 > col2:
        if row2 - row1 == col1 - col2:
            print('YES')
        else:
            print('NO')
    else:
        if row2 - row1 == col2 - col1:
            print('YES')
        else:
            print('NO')
