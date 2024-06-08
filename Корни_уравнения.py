from math import sqrt


def solve(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        if x1 < x2:
            return x1, x2
        else:
            return x2, x1
    elif D == 0:
        x = -(b / (2 * a))
        return x, x
    elif D < 0:
        return 'Нет корней'


print(solve(1, 2, 1))
