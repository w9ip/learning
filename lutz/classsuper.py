class Super:
    def __init__(self, value):
        print(value)


class Sub(Super):
    def __init__(self, value):
        Super.__init__(self, value)


i1 = Sub('hello')
# print(i1.__dict__)
# print(dir(i1))
