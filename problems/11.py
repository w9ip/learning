"""
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
заполнив её "диагоналями" в соответствии с образцом.
"""
n,m=map(int,input().split())
lst = [[col for col in range(1, m+1)] for row in range(1, n+1)]

nm = 0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                lst[i][j] = nm
for i in lst:
    print(*i)