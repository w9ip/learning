class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()
x.setdata('King Arthur')

y.setdata(3.14124)
print(x.__dict__)

x.data = 'New value'

print(x.__dict__)
x.anothername = 'spam'

print(x.__dict__)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


z = SecondClass()
z.setdata(42)
z.display()


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()

print(b)

a.mul(3)
print(a)
