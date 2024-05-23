n = int(input())
largest = 0
smallest = n % 10

while n != 0:
    last_digit = n % 10
    if last_digit > largest:
        largest = last_digit
    if last_digit <= smallest:
        smallest = last_digit
    n = n // 10
print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)
