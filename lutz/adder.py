class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other

class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data

class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)

x = adder(5)
x + 2
print(x.data)
# 2 + x