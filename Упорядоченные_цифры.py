n = int(input())
compare = n % 10
flag = True
while n != 0:
  last_digit = n % 10
  if not compare <= last_digit:
    flag = False
  compare = last_digit
  n = n // 10
  
if flag:
  print('YES')
else:
  print('NO')