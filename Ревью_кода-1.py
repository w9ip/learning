multiple = 1
counter = 0
for i in range(10):
  n = int(input())
  if n >= 0:
    multiple *= n
    counter += 1
if counter:
  print(counter, multiple, sep='\n')
else:
  print('NO')