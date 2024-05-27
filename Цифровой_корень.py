n = int(input())
total = 0
while n > 0:
    if n // 10 == 0:
        print(n)
        break
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n //= 10
    n = total
    total = 0
