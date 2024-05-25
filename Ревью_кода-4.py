n = int(input())
largest = -1
while n > 0:
	last_digit = n % 10
	if last_digit % 3 == 0 and last_digit > largest:
		largest = last_digit		
	n = n // 10
if largest == -1:
	print('NO')
else:
	print(largest)	print('NO')