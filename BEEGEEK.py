def is_prime(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += 1
    if total == 2 and n % 1 == 0 and n % n == 0:
        return True
    return False


def is_valid_password(password):
    password = password.split(':')
    if password[0] == password[0][::-1] and is_prime(int(password[1])) and int(password[2]) % 2 == 0 and len(
            password) == 3:
        return True
    return False


print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
