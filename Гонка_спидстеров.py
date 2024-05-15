n = int(input())  # Скорость Зума
k = int(input())  # Скорость Флеша

if n > k:
    print('NO')
elif n < k:
    print('YES')
else:
    print('Don\'t know')
