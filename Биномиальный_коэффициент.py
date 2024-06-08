from math import factorial


def compute_binom(n, k):
    return int(
        (factorial(n) / (factorial(k) * factorial(n - k)))
    )


n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
