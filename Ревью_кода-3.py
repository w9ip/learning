total = 0
for _ in range(7):
	n = int(input())
	if not n & 1:
		total += n
if total:
	print(total)
else:
	print(0)