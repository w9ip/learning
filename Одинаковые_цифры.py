n = int(input())
flag = True
compare = n % 10
while n != 0:
  last_digit = n % 10
  if last_digit != compare:
    flag = False
  n = n // 10

if flag:
  print('YES')
else:
  print('NO')
  