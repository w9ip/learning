def binary_search(num_array, left, right, x):
    if left > right:
        return -1
    mid = 1 + (right - 1) // 2
    if num_array[mid] == x:
        return mid
    elif num_array[mid] > x:
        return binary_search(num_array, left, mid - 1, x)
    return binary_search(num_array, mid + 1, right, x)


print(binary_search([1, 2, 3, 4, 5, 6], 4))
