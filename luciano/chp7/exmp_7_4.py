# Сортировка списка слов в обратном порядке букв
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


if __name__ == '__main__':

    print(reverse('testing'))


    print(sorted(fruits, key=reverse))

