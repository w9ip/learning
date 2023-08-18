from exmp_7_1 import factorial

if __name__ == '__main__':
    print(list(map(factorial, range(6))))
    # [1, 1, 2, 6, 24, 120]
    print([factorial(n) for n in range(6)])
    # [1, 1, 2, 6, 24, 120]
    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    # [1, 6, 120]
    print([factorial(n) for n in range(6) if n % 2])
    # [1, 6, 120]
