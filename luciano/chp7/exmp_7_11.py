from functools import reduce


# Вычисление факториала с помощью reduce и анонимной функции
def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))
