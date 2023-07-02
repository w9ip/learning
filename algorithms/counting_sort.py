def counting_sort(A, M):
    counts = [0] * M
    for v in A:
        counts[v] += 1
    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos+idx] = v
        pos += counts[v]
        v += 1
    return A
A = [0, 2, 4, 1, 3, 5]
M = 6

print(counting_sort(A, M))