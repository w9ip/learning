def my_max(A):
    m1 = A[0]
    m2 = A[1]
    if m1 < m2: m1, m2 = m2, m1
    for i in range(2, len(A)):
        if A[i] > m1 and m1 != m2:
            m2 = m1
            m1 = A[i]
        elif m2 < A[i]: m2 = A[i]
    return m1, m2

print(my_max([1, 2, 3, 4, 5, 6, 7]))
print(my_max([1, 2, 3, 4, 10, 16, 5, 6, 7]))
print(my_max([20, 3, 4, 10, 16, 5, 6, 7]))