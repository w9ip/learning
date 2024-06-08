def is_prime(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += 1
    if total == 2 and n % 1 == 0 and n % n == 0:
        return True
    return False


# объявление функции
def get_next_prime(num):
    while not is_prime(num + 1):
        num += 1
    return num + 1


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
