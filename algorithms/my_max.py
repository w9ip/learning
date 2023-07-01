def largest(A):
    my_max = A[0]
    for i in range(1, len(A)):
        if A[i] > my_max: my_max = A[i]
    return my_max

assert largest([1, 2, 3]) == 3
assert largest([1, 3, 2]) == 3
assert largest([3, 2, 1]) == 3

