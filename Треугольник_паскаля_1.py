from math import factorial


def compute_binom(n, k):
    return int(
        (factorial(n) / (factorial(k) * factorial(n - k)))
    )


n = int(input())
lst = []
for i in range(n + 1):
    lst.append(compute_binom(n, i))
print(lst)