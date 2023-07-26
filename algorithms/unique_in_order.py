"""
Реализовать функцию unique_in_order, которая принимает в качестве аргумента
последовательность и возвращает список элементов, в котором нет элементов с
одинаковым значением, расположенных рядом друг с другом и сохраняющих исходный
порядок следования элементов.
"""


def unique_in_order(s):
    lst = []
    if s and len(s) >= 1 and s[0]:
        lst.append(s[0])

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            lst.append(s[i])

    print(lst)


unique_in_order('')
unique_in_order([''])
unique_in_order('A')
unique_in_order('Ad')
unique_in_order('spam')
unique_in_order('AAAABBBCCDAABBB')
