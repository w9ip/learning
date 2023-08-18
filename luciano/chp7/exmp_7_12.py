from functools import reduce
from operator import mul


# Вычисление факториала с помощью reduce и operator.mul
def factorial(n):
    return reduce(mul, range(1, n + 1))
