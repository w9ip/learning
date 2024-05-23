n = int(input())

while n != 0:
    last_digit = n % 10
    print(last_digit, end='')
    n = n // 10
