class C2:
    ...


class C3:
    ...


class C1(C2, C3):
    def __init__(self, who):
        self.name = who


I1 = C1('bob')
I2 = C1('sue')

print(I1.name)
