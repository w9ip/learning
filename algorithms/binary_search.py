def binary_search(key: int, a: list):
    lo: int = 0
    hi: int = len(a)
    while lo <= hi:
        mid: int = lo + (hi - lo) // 2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid


if __name__ == '__main__':
    assert binary_search(3, [1, 2, 3, 4, 5]) == 2
    assert binary_search(1, [1, 2, 3, 4, 5]) == 0
    assert binary_search(4, [1, 2, 3, 4, 5]) == 3
