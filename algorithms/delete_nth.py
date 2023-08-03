def delete_nth(order, max_e):
    res = []
    for elm in order:
        if elm in res:  # Проверка есть ли elm в результирующем списке.
            if res.count(elm) < max_e:
                res.append(elm)  # Если меньше, добавляем в результирующий список.
        else:  # Если elm нет в результирующем списке.
            res.append(elm)  # Добавляем этот элемент.

    return res


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([20, 37, 20, 20, 21, 21], 1))
print(delete_nth([], 1))
