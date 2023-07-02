def largest_two_max(A):
    m1 = A[0]
    m2 = A[1]
    if m1 < m2: m1, m2 = m2, m1
    for i in range(2, len(A)):
        if A[i] > m1 and m1 != m2: # С использованием сравнения
            m2 = m1
            m1 = A[i]
        elif m2 < A[i]: m2 = A[i]
    return m1, m2

def sorting_two(A):
    return tuple(sorted(A, reverse=True)[::2]) # Создать из А новый отсортированный список и вернуть первые два его элемента.

def double_two(A):
    my_max = max(A) # Использовать встроенную функцию max()
    copy = list(A) # Создать дубликат списка
    copy.reamove(my_max) # Удалить из списка этот максимум (my_max)
    return (my_max, max(copy))

def mutable_two(A):
    idx = max(range(len(A)), key=A.__getitem__) # Трюк позволяющий найти индекс наибольшего значения, а не само наибольшее значение.
    my_max = A[idx] # Сохранить индекс наибольшего элемента в my_max
    del A[idx] # Удалить этот элемент из списка.
    second = max(A) # Найти еще один max() в усеченном списке.
    A.insert(idx, my_max)  # Вставить максимальный элемент списка обратно на место
    return (my_max, second)

print(mutable_two([1, 4, 6, 7, 2, 9, 3]))

A = [1, 4, 6, 7, 2, 9, 3]

idx = max(
    range(len(A)),
    key=A.__getitem__,
    )