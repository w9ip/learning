def recursive_binary_search(key, a):
    def rank(key, a, lo=0, hi=len(a)):
        # Если key пристутствует в a, его индекс не меньше lo и не больше hi.
        if lo > hi: return -1
        mid = lo + (hi - lo) // 2
        if key < a[mid]: return rank(key, a, lo, mid-1)
        elif key > a[mid]: return rank(key, a, mid + 1, hi)
        else: return mid
    return rank(key, a)

if __name__ == '__main__':
    assert recursive_binary_search(3, [1, 2, 3, 4, 5]) == 2
    assert recursive_binary_search(1, [1, 2, 3, 4, 5]) == 0
    assert recursive_binary_search(4, [1, 2, 3, 4, 5]) == 3