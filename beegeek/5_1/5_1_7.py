x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
for i in range(n):
    for j in range(n):
        if abs(y - i) == abs(x - j):
            board[i][j] = '*'
        if i == y or x == j:
            board[i][j] = '*'
board[y][x] = 'Q'

for row in board:
    print(*row)
