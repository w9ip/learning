n = int(input())
total = 0
while n != 0:
    ld = n % 10
    total += ld
    n //= 10
print(total)
