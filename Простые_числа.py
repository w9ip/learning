a, b = int(input()), int(input())
divisor_counter = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0 and i % 1 == 0:
            divisor_counter += j
    if i + 1 == divisor_counter:
        print(i)
    divisor_counter = 0
