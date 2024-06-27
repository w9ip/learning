def sum_matrix():
  n = int(input())
  a = [[int(e) for e in input().split()] for _ in range(n)]
  b = [[int(e) for e in input().split()] for _ in range(n)]
  c = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      c[i][j] = a[i][j] + b[i][j]
  return c
  

def dif_matrix():
  n = int(input())
  a = [[int(e) for e in input().split()] for _ in range(n)]
  b = [[int(e) for e in input().split()] for _ in range(n)]
  c = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      c[i][j] = a[i][j] - b[i][j]
  return c


def multiple_to_one_matrix():
  n = int(input())
  k = int(input())
  a = [[int(e) for e in input().split()] for _ in range(n)]
  c = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      c[i][j] = a[i][j] * k 
  return c
  
def multiple_matrix():
  # количество столбцов первой матрицы совпадает с количеством строк второй матрицы
  n, m = [int(e) for e in input().split()]
  a = [[int(e) for e in input().split()] for _ in range(n)]
  input()
  m, k = [int(e) for e in input().split()]
  b = [[int(e) for e in input().split()] for _ in range(m)]
  c = [[0 for i in range(n)] for _ in range(k)]
  print(f'n:{n}, m:{m}, k:{k}, a:{a}, b:{b}, c:{c}')
  for i in range(n):
    r = 0
    for j in range(m):
      print(a[i][r], b[r][j], end=' ')
      r += 1
    print()
  return c
print(multiple_matrix())