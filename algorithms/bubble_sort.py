# O(n^2)

def bubble_sort(array):
    for _ in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    assert bubble_sort([2, 3, 4, 1, 6, 7, 5]) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort([2, 8, 10, 23, 78, 90, 3, 4, 1, 6, 7, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 10, 23, 78, 90]
