matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[-(j+1)][i], end=' ')
    print()
