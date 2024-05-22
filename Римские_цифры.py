# 4 = IX
# 5 = V
# 9 = IX
# 10 = X

n = int(input())

if n < 0 or n > 10:
    print('ошибка')

if n < 4:
    print('I' * n)
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif n < 9:
    print('V' + 'I' * (n - 5))
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
