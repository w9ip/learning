total = 0
for i in range(1, int(input()) + 1):
    condition = i * i % 10 in (2, 5, 8)
    if condition:
        total += i
print(total)
