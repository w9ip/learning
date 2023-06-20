def gen():
    x = 0
    x += 1
    yield x


g = gen()
next(g)
