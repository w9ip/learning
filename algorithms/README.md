## Реализовать функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список элементов, в котором нет элементов с одинаковым значением, расположенных рядом друг с другом и сохраняющих исходный порядок следования элементов:

[unique_in_order](unique_in_order.py)

```python
def unique_in_order(s):
    lst = []
    if s and len(s) >= 1 and s[0]:
        lst.append(s[0])

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            lst.append(s[i])

    print(lst)
```

## Отсортировать только нечетные числа, четные остаются на своих позициях.

[sort_only_odds](sort_only_odds.py)

```python
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
```
