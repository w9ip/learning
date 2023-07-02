from time import time

def is_palindrome1(w):
    return w[::-1] == w

def is_palindrome2(w):
    while len(w) > 1:
        if w[0] != w[-1]:
            return False
        w = w[1:-1]

def is_palindrome0(A):
    r = -1
    for l in range(len(A)//2):
        if A[l] == A[r]:
            r += -1
        else:
            return False
    return True

def test(func, N):
    start = time()
    for i in range(N):
        func('КАЗАККАЗАК')
    end = start - time()
    print(f'Запущено {N} раз, время выполнения {func.__name__} {end}')
          
test(is_palindrome0, 1000)
test(is_palindrome1, 1000)
test(is_palindrome2, 1000)

# print(is_palindrome0('КАЗАККАЗАК'))