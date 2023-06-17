# https://stepik.org/lesson/416757/step/1?unit=406265

std_read = input()

rows, cols = int(std_read[0]), int(std_read[2])

res = []

for row in range(rows):
    res.append([])
    for col in range(cols):
        if col % 2 == 0:
            if row % 2 == 0:
                res[row].append('.')
            else:
                res[row].append('*')
        elif col % 2 != 0:
            if row % 2 != 0:
                res[row].append('.')
            else:
                res[row].append('*')
    print(*res[row])
