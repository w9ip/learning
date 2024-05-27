a, b = int(input()), int(input())
largest_n = 0
total_divisor = 0
total_divisor_tmp = 0

for i in range(b, a - 1, -1):
    for j in range(1, i + 1):
        if i % j == 0:
            total_divisor_tmp += j
    if total_divisor < total_divisor_tmp:
        largest_n = i
        total_divisor = total_divisor_tmp
    total_divisor_tmp = 0
print(largest_n, total_divisor)
