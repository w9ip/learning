n = int(input())
total_divisor_tmp = 0
for i in range(1, n+1):
    for j in range(1, i + 1):
        if i % j == 0:
            total_divisor_tmp += 1
    print(i, '+' * total_divisor_tmp, sep='')
    total_divisor_tmp = 0