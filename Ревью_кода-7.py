n = int(input())
total = 0

while n > 0:
    last_digit = n % 10
    if not last_digit & 1:
        total += last_digit
    n //= 10
if total:
    print(total)
else:
    print(0)
