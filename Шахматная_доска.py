row1 = int(input())
col1 = int(input())

row2 = int(input())
col2 = int(input())

cor1 = 0
cor2 = 0

if row1 & 1:
    if col1 & 1:
        cor1 = 0
    else:
        cor1 = 1
else:
    if col1 & 1:
        cor1 = 1
    else:
        cor1 = 0

if row2 & 1:
    if col2 & 1:
        cor2 = 0
    else:
        cor2 = 1
else:
    if col2 & 1:
        cor2 = 1
    else:
        cor2 = 0

print('YES' if cor1 == cor2 else 'NO')
