class Iters:
    def __init__(self, value) -> None:
        self.data = value
    def __getitem__(self, i):    # Запасной вариант для итерации
                                 # Также для индексирования, нарезания
        print('get[%s]:' % i, end=' ')
        return self.data[i]
    def __iter__(self):          # Предпочтительнее для итерации
        print('iter=> ', end='')  # Допускает только один активный проход.
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):  # Предпочтительнее для операции in
        print('contains: ', end='')
        return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    print(X[1])
    for i in X:
        print(i, end=' | ')
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break