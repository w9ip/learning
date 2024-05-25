total = 0
largest = -10**6
for _ in range(4):
	n = int(input())
	if n < 0:
		total += n
		if n > largest:
			largest = n
if total:
	print(total, largest, sep='\n')
else:
	print('NO')e:
	print('NO')