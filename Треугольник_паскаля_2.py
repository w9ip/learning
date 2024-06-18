from math import factorial


def compute_binom(n, k):
    return int(
        (factorial(n) / (factorial(k) * factorial(n - k)))
    )


def pascal_triangle(n):
    lst = []
    for i in range(n + 1):
        lst.append(compute_binom(n, i))
    return lst


for i in range(int(input())):
    print(*pascal_triangle(i))
