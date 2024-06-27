d = {}
c = 0
with open('tests.txt', 'r', encoding='UTF8') as tests:
    title = next(tests)
    print(title)
    for s in tests:
        print(s)
        print(repr(s))
print(d)