class A:
    xa = 'xa in class A'

    def __init__(self):
        xai = 'xai in class A'


class B:
    xb = 'xb in class A'

    def __init__(self):
        xbi = 'xbi in class A'


class C(A, B):
    xc = 'xc in class A'

    def __init__(self):
        xci = 'xci in class A'


if __name__ == '__main__':
    i = C()
    A.foo = 'foo'
    print(i.xa)
    print(dir(i))
    print(type(i))
    print(type(C))
    print(C.__module__)
    print('-' * 40)
