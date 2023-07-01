def recursive_binary_search(key, a):
    def searcher(key, a, left=0, right=len(a)):
        if left > right: return -1
        mid = left + (right - left) // 2
        if key < a[mid]:
            return searcher(key, a, left, mid - 1)
        elif key > a[mid]:
            return searcher(key, a, mid + 1, right)
        else:
            return mid

    return searcher(key, a)


if __name__ == '__main__':
    assert recursive_binary_search(3, [1, 2, 3, 4, 5]) == 2
    assert recursive_binary_search(1, [1, 2, 3, 4, 5]) == 0
    assert recursive_binary_search(5, [1, 2, 3, 4, 5]) == 4
