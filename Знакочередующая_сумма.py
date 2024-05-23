total = 1
for i in range(2, int(input()) + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)
