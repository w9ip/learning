a = [5, 1, 3, 2, 0, 98]
for i in range(len(a) - 1):
    largest_item_index = i
    for j in range(i + 1, len(a)):
        if a[largest_item_index] > a[j]:
            largest_item_index = j
    a[i], a[largest_item_index] = a[largest_item_index], a[i]
print(a)
